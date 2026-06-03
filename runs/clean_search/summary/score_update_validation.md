# clean_search Score Update Validation

Date: 2026-06-03

Scope: all 35 samples under `runs/clean_search`.

## Consistency Check

- `report.json` files found: 35
- `report.md` files found: 35
- Missing `report.md`: 0
- `overall` mismatches between `report.md` and `report.json`: 0
- `citation_quality` mismatches between `report.md` and `report.json`: 0

## All-Sample Means

- Overall mean: 7.2591
- Citation quality mean: 8.2523

## Score Changes Versus Previous Summary CSV

Only one score changed:

| Path | Metric | Previous | Current |
|---|---:|---:|---:|
| `openclaw+ds-v4-pro\sim_prompt\sim_prompt_PaperA` | overall | 7.88 | 7.47 |

No `citation_quality` score changed versus the previous `clean_search_scores_full.csv`.

## Regenerated Outputs

The existing summary generation script was rerun with:

```powershell
D:\Anaconda\envs\llm\python.exe analysis\build_clean_search_figures.py --root runs\clean_search --out runs\clean_search\summary
```

This refreshed the summary CSV/Markdown/LaTeX files and the related PDF/PNG charts in `runs/clean_search/summary`.
