# Omics Method Research Skills

面向单细胞与空间组学计算方法开发的证据驱动工作流。
**分发版本 0.2.1；科研知识版本 0.2.0。29 个可发现入口；133 个共享科研资料文件。**

本仓库是可直接发布到 GitHub 的源码树，不是一个只能下载 ZIP 的仓库。
`OWNER/omics-method-research-skills` 均为发布前占位符，发布人需要替换 OWNER。
尚未声明已经上传 GitHub，也未在真正的 Codex 客户端完成加载验收。

## 从 GitHub 安装：Linux / 远端 SSH

在 Codex **实际执行文件读写和命令的远端环境**安装。只需要已有 Git 和 Python 3.8+；
加载这些说明不需要安装 PyTorch、R、CUDA、Node 或 API key。

```bash
# 发布完成后，把 OWNER 改为真实 GitHub 用户或组织名
REPO="OWNER/omics-method-research-skills"
mkdir -p "$HOME/ai-skills"
git clone "https://github.com/$REPO.git" "$HOME/ai-skills/omics-method-research-skills"
cd "$HOME/ai-skills/omics-method-research-skills"

# 先检查下载的源码，再预览并安装
python3 scripts/validate_repo.py
python3 install_codex.py --scope user --profile all --dry-run
python3 install_codex.py --scope user --profile all
python3 install_codex.py --scope user --check
```

不要在已有、包含手工修改的 clone 上重复执行 `git clone`。更新流程见安装指南。
仓库私有时应使用已获该仓库权限的 Git/SSH 或 `gh repo clone`；不要把 PAT 写进 URL、脚本或提示词。

## Nature-skills 风格：npx skills

使用第三方 Vercel skills CLI（不是 OpenAI 内置命令）。先核对实际 Node 版本与 CLI engines；
本次查阅的 CLI 源码 `1.5.22` 要求 Node >=22.20.0。本包的默认 Git+Python 路线不依赖它。

```bash
npx skills add OWNER/omics-method-research-skills --list
npx skills add OWNER/omics-method-research-skills --global --agent codex \
  --skill '*' --copy --yes
```

只装 OT/FM 时，**同时安装 `omics-research`**：

```bash
npx skills add OWNER/omics-method-research-skills --global --agent codex \
  --skill omics-research --skill omics-ot --skill omics-flow-matching --copy --yes
```

只安装一个专用入口不会自动把相邻的共享技能带上。不要假设 npx 或 `$skill-installer` 会解析本包的依赖。
这些 npx 命令依官方 CLI 文档与源码编写；本轮未完成 npx 端到端运行。详见 `verification/REPORT_ZH.md`。

## 直接在 Codex 中要求安装

```text
请从 https://github.com/OWNER/omics-method-research-skills 安装这组技能。
先读取 README.md、docs/INSTALL_ZH.md 和 scripts/install_codex.py，检查实际执行环境。
在当前用户的 ~/.agents/skills 中安装全部入口和共享资料。
先运行 dry-run，再正式安装并 --check；不要安装科研依赖或运行训练。
已有同名技能时停止覆盖，检查是否需要文档中的 --migrate-v02。
最后列出实际安装路径、版本与校验结果。
```

存在 `$skill-installer` 的客户端还可明确要求从同一 GitHub 仓库下载
`skills/omics-research` 与所选 `skills/omics-*` 目录，到同一个技能根目录。

## 使用

新开 Codex 会话，明确点名技能：

```text
$omics-research
读取当前项目设计，选择完成本轮决策需要的技能，不启动训练。
```

```text
$omics-ot
$omics-flow-matching
审查当前 UOT 配对、质量、条件路径、速度目标与 ODE 验收。
只生成方法合同和最小测试计划。
```

不确定调用哪个入口时使用 `$omics-research`。
它本身包含全部工作流；其他 28 个入口是方便显式调用的快捷方式。
所有资料按需读取，不必一次加载整套文献。

## 目录

```text
.
├── README.md
├── install_codex.py
├── catalog.json
├── skills/
│   ├── omics-research/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── library/             # 一份共享科研资料
│   │       ├── GUIDE.md         # 原总路由，非重复注册入口
│   │       ├── skills/*/GUIDE.md
│   │       ├── knowledge/
│   │       ├── references/
│   │       ├── lab/
│   │       └── ...
│   ├── omics-ot/SKILL.md
│   ├── omics-flow-matching/SKILL.md
│   └── ...                     # 共 29 个原生入口
├── scripts/                    # 安装、验证、打包、发布
├── docs/
├── tests/
├── verification/
├── provenance/
├── plugin.json                 # 可选 portable plugin
├── .codex-plugin/plugin.json    # 兼容插件清单
└── .agents/plugins/marketplace.json
```

内部 29 个 `SKILL.md` 已改名 `GUIDE.md` 并更新引用，以免被递归扫描误识别为额外技能。
全部 133 个文件都保留；逐文件输入/输出哈希和改动范围见 `provenance/library_transform.json`。
**旧版文件不再逐字节相同，但改动仅用于路径、命名、一处历史沙箱路径脱敏和 TSV 换行标准化。**

## 更多入口

- [安装、分类安装、更新和旧版迁移](docs/INSTALL_ZH.md)
- [发布源码与 ZIP 到 GitHub](docs/PUBLISH_ZH.md)
- [完整技能分类](docs/SKILL_CATALOG.md)
- [可复制 Codex 提示词](docs/PROMPTS_ZH.md)
- [本轮实际测试与边界](verification/REPORT_ZH.md)
- [许可证决策与来源](LICENSE_AND_ATTRIBUTION.md)

本包不等于 Nature-skills 官方扩展，未复制其源代码。
科研知识仍为文献驱动、带有限数值检查的工作流；历史 toy tests 不等于原论文复现或临床验证。
