# Related Work Evaluator

This is the local RWEval pipeline adapted for this project. It evaluates generated Related Work against ground-truth Related Work with code metrics, LLM judgments, and DeepXiv-backed citation normalization/evidence retrieval.

## Inputs

Each sample contains:

- `s_text`: generated Related Work to evaluate.
- `s_references`: reference list used by the generated Related Work.
- `g_text`: ground-truth Related Work.
- `g_references`: ground-truth reference list. Use an empty string if unavailable.

The `evaluate-files` command reads these files from a directory:

```text
s_text.txt
s_reference.txt
g_text.txt
g_reference.txt
```

## Configuration

Create `.env` from `.env.example`:

```text
LLM_API_BASE_URL=
LLM_API_KEY=
LLM_MODEL=
LLM_TIMEOUT_SECONDS=60
LLM_JSON_MODE=false

DEEPXIV_TOKEN=

RW_EVAL_CACHE_DIR=.cache/rw_eval
```

The LLM endpoint must be OpenAI-compatible at `POST /chat/completions`. DeepXiv is used by default for reference normalization and claim-citation evidence retrieval.

## Run Examples

```bash
python -m rw_eval.cli evaluate-files \
  --directory examples/sample1 \
  --output outputs_local/sample1_report.json \
  --markdown-output outputs_local/sample1_report.md
```

Use `examples/sample2` for the second sample.

## Evaluate JSON

```bash
python -m rw_eval.cli evaluate \
  --input examples/sample1/sample_input.json \
  --output outputs_local/sample1_report.json \
  --markdown-output outputs_local/sample1_report.md
```

## Disable DeepXiv

Use this only for local parser/smoke checks when DeepXiv is intentionally unavailable:

```bash
python -m rw_eval.cli evaluate-files \
  --directory examples/sample1 \
  --output outputs_local/sample1_report.json \
  --markdown-output outputs_local/sample1_report.md \
  --no-deepxiv
```

`--no-semantic-scholar` remains as a deprecated alias for `--no-deepxiv`.

## Modules

- `rw_eval/pipeline.py`: end-to-end evaluation.
- `rw_eval/external/deepxiv.py`: DeepXiv client.
- `rw_eval/llm/`: LLM extraction and judging.
- `rw_eval/scoring/`: metric scoring.
- `rw_eval/reporting/`: JSON and Markdown reports.
- `configs/rubric.json`: weights, caps, thresholds, and DeepXiv defaults.

## Verification

```bash
python -B -m unittest discover -s tests
```

```bash
python -B -c "import ast, pathlib; files=list(pathlib.Path('rw_eval').rglob('*.py'))+list(pathlib.Path('tests').rglob('*.py')); [ast.parse(p.read_text(encoding='utf-8'), filename=str(p)) for p in files]; print(f'parsed {len(files)} python files')"
```
