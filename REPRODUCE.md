# 最简复现流程

这份说明给第一次接触项目的同学使用。目标是复跑仓库里已经准备好的 RWEval 评测结果，不包含重新调用 OpenClaw 生成 `s_text.txt` / `s_reference.txt`。

## 1. 克隆仓库

```powershell
cd D:\college\llm
git clone https://github.com/Harry050118/final_proj.git
cd final_proj
```

如果你不想放在 `D:\college\llm`，也可以放到其他目录。后面的命令把 `D:\college\llm\final_proj` 换成你自己的项目路径即可。

## 2. 创建 Python 环境

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install deepxiv-sdk
```

## 3. 配置 `.env`

在项目根目录 `final_proj\.env` 新建文件，写入下面内容。不要把真实 key 提交到 GitHub。

```text
DEEPXIV_API_TOKEN=填你的DeepXiv token
LLM_API_BASE_URL=填OpenAI兼容接口地址
LLM_API_KEY=填你的LLM API key
LLM_MODEL=填模型名

LLM_TIMEOUT_SECONDS=300
LLM_REQUEST_RETRIES=0
LLM_JSON_RETRIES=1
LLM_JSON_MODE=true
RW_EVAL_CACHE_DIR=evaluation/RWEval/.cache/rw_eval
```

`LLM_API_BASE_URL` 需要是 OpenAI-compatible 接口，能访问 `POST /chat/completions`。

## 4. 检查命令入口

```powershell
cd D:\college\llm\final_proj\evaluation\RWEval
python -m rw_eval.cli --help
```

能看到 `evaluate`、`batch`、`evaluate-files`、`package-sample` 这些命令就说明入口正常。

## 5. 跑一个样本

先跑最简单推荐样本：`openclaw+ds-v4-pro / sim_prompt / source`。

```powershell
cd D:\college\llm\final_proj\evaluation\RWEval

python -m rw_eval.cli evaluate-files `
  --directory "..\..\runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source" `
  --sample-id "sim_prompt-source" `
  --output "..\..\runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source\report.json" `
  --markdown-output "..\..\runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source\report.md" `
  --env "..\..\.env"
```

跑完后查看：

```text
runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source\sample_input.json
runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source\report.json
runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source\report.md
```

## 6. 跑其他样本

如果要跑别的样本，只需要把命令里的 `source` 换成下面任意一个：

```text
07794
11662
12299
researcher
source
```

例如跑 `07794`，就把路径里的：

```text
\sim_prompt\source
```

改成：

```text
\sim_prompt\07794
```

同时建议把 `--sample-id "sim_prompt-source"` 改成 `--sample-id "sim_prompt-07794"`。

## 7. 跑 skill 或 kimi 版本

如果要跑 skill 版本，把路径里的：

```text
sim_prompt
```

改成：

```text
sim_prompt+skill
```

如果要跑 kimi 结果，把路径里的：

```text
openclaw+ds-v4-pro
```

改成：

```text
openclaw+kimi-k2.6
```

建议第一次复现先跑：

```text
runs\clean_search\openclaw+ds-v4-pro\sim_prompt\source
```

确认流程没问题后，再换其他样本或版本。

## 8. 常见问题

- 如果提示缺少 `LLM_API_BASE_URL`、`LLM_API_KEY` 或 `LLM_MODEL`，检查 `.env` 是否在项目根目录，以及命令里是否写了 `--env "..\..\.env"`。
- 如果提示 `No module named deepxiv_sdk`，执行 `python -m pip install deepxiv-sdk`。
- 如果没有 DeepXiv token，只能临时加 `--no-deepxiv` 做命令链路测试；这不是完整评测。
- 评测依赖 LLM，换模型或接口后，分数可能和原结果略有差异。
