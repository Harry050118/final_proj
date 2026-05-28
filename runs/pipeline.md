# RWEval 评测流程

本项目在 `runs/clean_search` 下保留两个 Clean Search 实验目录：

```text
runs/clean_search/
  diff_prompt/          # 无 skill 实验
  sim_prompt+skill/     # 有 skill 实验
```

每篇论文放在对应实验目录下的 `<paper_id>` 子目录中，并保持 RWEval 原生四文件格式。当前默认示例使用有 skill 实验：

```text
runs/clean_search/sim_prompt+skill/evotest/
```

## 1. 准备实验目录

创建或选择一个实验目录：

```powershell
cd D:\college\llm\final_proj
New-Item -ItemType Directory -Force -Path runs\clean_search\sim_prompt+skill\evotest
```

目录中最终应包含以下四个 RWEval 输入文件：

```text
runs\clean_search\sim_prompt+skill\evotest\
  s_text.txt
  s_reference.txt
  g_text.txt
  g_reference.txt
```

可选审计文件：

```text
runs\clean_search\sim_prompt+skill\evotest\trace.md
```

`trace.md` 只用于记录 OpenClaw/DeepXiv 的检索和引用决策过程。RWEval 命令不会读取它。

## 2. 给 OpenClaw 的当前命令

把 `runs/command.txt` 中的命令交给 OpenClaw。当前命令指向：

```text
runs/clean_search/sim_prompt+skill/evotest
```

如需运行无 skill 实验，只修改输出目录到对应论文目录，例如：

```text
Output directory: runs/clean_search/diff_prompt/evotest
```

## 3. 添加 Ground Truth 文件

OpenClaw 完成后，把 ground truth 文件放到同一个实验目录：

```text
runs\clean_search\sim_prompt+skill\evotest\g_text.txt
runs\clean_search\sim_prompt+skill\evotest\g_reference.txt
```

OpenClaw 不允许读取这些文件。它们只给 RWEval 使用。

## 4. 评测前检查目录

```powershell
cd D:\college\llm\final_proj
Get-ChildItem runs\clean_search\sim_prompt+skill\evotest
```

正式评测前，至少应看到以下四个核心文件：

```text
s_text.txt
s_reference.txt
g_text.txt
g_reference.txt
```

如果四个文件不齐，不要运行最终评测。

## 5. 运行 RWEval

```powershell
cd D:\college\llm\final_proj\evaluation\RWEval
$env:LLM_TIMEOUT_SECONDS="300"
$env:LLM_REQUEST_RETRIES="0"
$env:LLM_JSON_RETRIES="1"
$env:LLM_JSON_MODE="true"

python -m rw_eval.cli evaluate-files `
  --directory ..\..\runs\clean_search\sim_prompt+skill\evotest `
  --sample-id sim_prompt+skill-evotest `
  --output ..\..\runs\clean_search\sim_prompt+skill\evotest\report.json `
  --markdown-output ..\..\runs\clean_search\sim_prompt+skill\evotest\report.md `
  --env ..\..\.env
```

这个命令会读取四个 txt 文件，并写出：

```text
runs\clean_search\sim_prompt+skill\evotest\sample_input.json
runs\clean_search\sim_prompt+skill\evotest\report.json
runs\clean_search\sim_prompt+skill\evotest\report.md
```

`sample_input.json` 由 RWEval 自动生成，不需要手写。

## 6. 无 DeepXiv 的连通性测试

只有在 DeepXiv 凭证不可用时，才用下面命令检查文件解析和命令链路：

```powershell
cd D:\college\llm\final_proj\evaluation\RWEval
$env:LLM_TIMEOUT_SECONDS="300"
$env:LLM_REQUEST_RETRIES="0"
$env:LLM_JSON_RETRIES="1"
$env:LLM_JSON_MODE="true"

python -m rw_eval.cli evaluate-files `
  --directory ..\..\runs\clean_search\sim_prompt+skill\evotest `
  --sample-id sim_prompt+skill-evotest `
  --output ..\..\runs\clean_search\sim_prompt+skill\evotest\report.json `
  --markdown-output ..\..\runs\clean_search\sim_prompt+skill\evotest\report.md `
  --env ..\..\.env `
  --no-deepxiv
```

`--no-deepxiv` 不是完整评测，因为引用标准化和证据检索会被关闭。
