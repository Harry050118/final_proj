from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path("papers")
RAW = ROOT / "raw"
ANON = ROOT / "anonymized_inputs"
GT = ROOT / "ground_truth_related_work"
FONT_PATH = Path(r"C:\Windows\Fonts\times.ttf")
FONT_NAME = "TimesNewRoman"


CONFIGS = [
    {
        "paper_id": "evotest",
        "glob": "EvoTest_*.pdf",
        "abstract": r"ABSTRACT",
        "related": r"2\s*RELATED\s*WORK",
        "after_related": r"3\s*THEJERICHOTEST-TIMELEARNING",
        "refs": r"REFERENCES",
        "notes": "Boundary markers: ABSTRACT, 2 RELATEDWORK, 3 THE JERICHO..., REFERENCES.",
    },
    {
        "paper_id": "mcp_security_bench",
        "glob": "MCP Security Bench*.pdf",
        "abstract": r"ABSTRACT",
        "related": r"2\s*RELATED\s*WORK",
        "after_related": r"3\s*PRELIMINARY\s*ANDTHREATMODEL",
        "refs": r"REFERENCES",
        "notes": "Boundary markers: ABSTRACT, 2 RELATEDWORK, 3 PRELIMINARY..., REFERENCES.",
    },
    {
        "paper_id": "mem1",
        "glob": "MEM1_*.pdf",
        "abstract": r"Abstract",
        "related": r"2\s*Related\s*Work",
        "after_related": r"3\s*MEM1\b",
        "refs": r"References",
        "notes": "Boundary markers: Abstract, 2 Related Work, 3 MEM1, References.",
    },
    {
        "paper_id": "traject_bench",
        "glob": "TRAJECT-Bench*.pdf",
        "abstract": r"ABSTRACT",
        "related": r"2\s*RELATED\s*WORK",
        "after_related": r"3\s*DATACONSTRUCTION",
        "refs": r"REFERENCES",
        "notes": "Boundary markers: ABSTRACT, 2 RELATEDWORK, 3 DATACONSTRUCTION, REFERENCES.",
    },
    {
        "paper_id": "mandela_agents",
        "glob": "When Agents*.pdf",
        "abstract": r"ABSTRACT",
        "related": r"2\s*RELATED\s*WORK",
        "after_related": r"3\s*MANBENCH",
        "refs": r"REFERENCES",
        "notes": "Boundary markers: ABSTRACT, 2 RELATEDWORK, 3 MANBENCH, REFERENCES.",
    },
]


TITLE_OR_HEADER_PATTERNS = [
    r"Published as a conference paper at ICLR 2026",
    r"TRAJECT-Bench: A Trajectory-Aware Benchmark for Evaluating Agentic Tool Use",
    r"EvoTest: Evolutionary Test-Time Learning for Self-Improving Agentic Systems",
    r"MCP Security Bench \(MSB\): Benchmarking Attacks Against Model Context Protocol in LLM Agents",
    r"MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents",
    r"When Agents .Misremember. Collectively: Exploring the Mandela Effect in LLM-Based Multi-Agent Systems",
]


REMOVED_CONTENT = (
    "Title; Related Work excluded from anonymized input; References/Bibliography; "
    "Figures/Tables; Figure/Table captions; DOI/arXiv/full paper identifiers where detected"
)


def read_pdf_text(path: Path) -> str:
    return "\n".join((page.extract_text() or "") for page in PdfReader(str(path)).pages)


def find_one(pattern: str, text: str, label: str, start: int = 0) -> int:
    match = re.search(pattern, text[start:], flags=re.IGNORECASE)
    if not match:
        raise RuntimeError(f"Could not find {label}: {pattern}")
    return start + match.start()


def resolve_pdf(glob_pattern: str) -> Path:
    matches = sorted(RAW.glob(glob_pattern))
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one match for {glob_pattern}, found {len(matches)}")
    return matches[0]


def remove_caption_blocks(text: str) -> str:
    cleaned_lines: list[str] = []
    skipping_caption = False
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^(Figure|Fig\.|Table)\s*[0-9A-Za-z.]*\s*[:.]", stripped):
            skipping_caption = True
            continue
        if skipping_caption:
            if (
                not stripped
                or re.match(r"^(?:[1-9]|10)(?:\.\d+)*\s+", stripped)
                or re.match(r"^[A-Z][A-Z0-9 &/,-]{5,}$", stripped)
            ):
                skipping_caption = False
            else:
                continue
        cleaned_lines.append(line.rstrip())
    return "\n".join(cleaned_lines)


def clean_text(text: str) -> str:
    text = text.replace("\r", "\n")
    for pattern in TITLE_OR_HEADER_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = re.sub(r"https?://\S+", "[URL removed]", text)
    text = re.sub(r"\barXiv\s*:?\s*\d{4}\.\d{4,5}(?:v\d+)?\b", "[arXiv removed]", text, flags=re.IGNORECASE)
    text = re.sub(r"\b10\.\d{4,9}/\S+", "[DOI removed]", text, flags=re.IGNORECASE)
    text = remove_caption_blocks(text)
    lines = []
    for line in text.splitlines():
        if re.fullmatch(r"\s*\d+\s*", line):
            continue
        if re.search(r"\[arXiv removed\]", line, flags=re.IGNORECASE):
            continue
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def register_font() -> None:
    if FONT_PATH.exists():
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH)))
    else:
        raise RuntimeError(f"Font not found: {FONT_PATH}")


def escape_pdf_text(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\u00ad", "")
    )


def write_pdf(path: Path, body: str) -> None:
    style = ParagraphStyle(
        "paper-body",
        fontName=FONT_NAME,
        fontSize=10,
        leading=13,
        firstLineIndent=0,
        spaceAfter=6,
    )
    doc = SimpleDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    story = []
    for block in re.split(r"\n\s*\n", body.strip()):
        block = re.sub(r"\s*\n\s*", " ", block).strip()
        if not block:
            continue
        story.append(Paragraph(escape_pdf_text(block), style))
        story.append(Spacer(1, 4))
    doc.build(story)


def residue_check(text: str) -> str:
    residue = []
    checks = [
        ("DOI", r"\b10\.\d{4,9}/\S+"),
        ("arXiv", r"\barXiv\s*:?\s*\d{4}\.\d{4,5}(?:v\d+)?\b"),
        ("References heading", r"\bReferences\b"),
        ("Related Work heading", r"\bRelated\s*Work\b"),
    ]
    for label, pattern in checks:
        if re.search(pattern, text, flags=re.IGNORECASE):
            residue.append(label)
    return "none_detected" if not residue else "; ".join(residue)


def main() -> None:
    register_font()
    ANON.mkdir(parents=True, exist_ok=True)
    GT.mkdir(parents=True, exist_ok=True)

    rows = []
    for config in CONFIGS:
        source_pdf = resolve_pdf(config["glob"])
        full_text = read_pdf_text(source_pdf)

        abstract_start = find_one(config["abstract"], full_text, "abstract")
        related_start = find_one(config["related"], full_text, "Related Work", abstract_start)
        after_related_start = find_one(
            config["after_related"], full_text, "section after Related Work", related_start
        )
        references_start = find_one(config["refs"], full_text, "References", after_related_start)

        anonymized_body = clean_text(
            full_text[abstract_start:related_start] + "\n\n" + full_text[after_related_start:references_start]
        )
        related_body = clean_text(full_text[related_start:after_related_start])

        anonymized_path = ANON / f"{config['paper_id']}.pdf"
        related_path = GT / f"{config['paper_id']}.pdf"
        write_pdf(anonymized_path, anonymized_body)
        write_pdf(related_path, related_body)

        figure_status = (
            "figure_or_table_mentions_remain_no_caption_heading_detected"
            if re.search(r"\b(Figure|Fig\.|Table)\b", anonymized_body)
            else "no_obvious_caption_residue"
        )
        rows.append(
            {
                "paper_id": config["paper_id"],
                "raw_pdf": source_pdf.as_posix(),
                "sha256": hashlib.sha256(source_pdf.read_bytes()).hexdigest(),
                "anonymized_input": anonymized_path.as_posix(),
                "ground_truth_related_work": related_path.as_posix(),
                "removed_content": REMOVED_CONTENT,
                "identifier_residue_check": residue_check(anonymized_body),
                "figure_information_after_removal": figure_status,
                "notes": config["notes"],
            }
        )

    manifest_path = ROOT / "paper_split_manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"created {len(rows)} paper splits")


if __name__ == "__main__":
    main()
