# 安装与使用

## 1. 选一条安装路线，不要重复注册

默认推荐 `git clone + python3 install_codex.py`：它只使用标准库，自动包含总路由依赖，
支持文件校验、明确备份、增量更新和上一个 v0.2-codex 安装器的迁移。

替代方式是第三方 `npx skills add` 或 Codex 的 `$skill-installer`。
二者按目录安装，选择专用入口时必须把 `omics-research` 一起安装。
不要对同一组本地目录交替使用 npx、自带安装器和插件安装；它们的所有权/更新记录不同。

安装默认用户目录为 `~/.agents/skills`。项目安装采用 `<project>/.agents/skills`。
已有特殊客户端路径必须先确认；`--dest /explicit/skills` 用于明确覆盖默认目标，不应猜测。
系统内置 `$skill-installer` 在不同版本可能采用不同默认目录，须显式检查安装输出或指定目标。

## 2. 用户级、项目级和分类

在 clone 根目录：

```bash
python3 install_codex.py --list
python3 install_codex.py --scope user --profile all --dry-run
python3 install_codex.py --scope user --profile all
python3 install_codex.py --scope user --check
```

首次只装一类时，用以下命令**替代** `--profile all`：

```bash
python3 install_codex.py --profile dynamics
# 或
python3 install_codex.py --profile statistics
# 或
python3 install_codex.py --only omics-programs omics-robustness
# 或只装总路由（仍能按编号使用全部工作流）
python3 install_codex.py --profile router
```

| profile | 覆盖原编号；均额外包含总路由 |
|---|---|
| all | 01–28 |
| router | 仅总入口，但含完整资料 |
| design | 01、02、03、04、05、06、12、17 |
| spatial | 03、04、05、06、07、10、11、13、24、28 |
| dynamics | 03、09、12、14、23、25、26、28 |
| statistics | 03、13、14、15、21、22、23、28 |
| reproduction | 05、13、17、19、20、27 |
| writing | 02、16、18、22、23 |

项目级替代方案（路径是示例，换成实际项目）：

```bash
python3 install_codex.py --scope project --project /path/to/project --profile all
python3 install_codex.py --scope project --project /path/to/project --check
```

未自动安装科研依赖、触发下载/训练、创建 cron/hooks、修改项目 AGENTS.md 或 Codex 配置。
安装结果是文件就绪，不是客户端已加载，更不是实验复现。

## 3. 已安装上一版 v0.2-codex

先不要运行 npx 去覆盖旧入口。使用：

```bash
python3 install_codex.py --scope user --profile all --migrate-v02 --dry-run
python3 install_codex.py --scope user --profile all --migrate-v02
python3 install_codex.py --scope user --check
```

迁移只接受旧安装器的已知所有权清单，并检查原入口是否保持原哈希。
发现手工编辑、符号链接、未知同名目录或错误清单会停止，不强行覆盖。
旧入口备份到 `.agents/omics-method-research-github/backups/<timestamp>/skills/`；
旧共享库 `.agents/omics-method-research/library/` 保留，不自动删除。
今后使用新安装器，不再对迁移后的入口调用旧版 `--check`。

## 4. 更新

记录当前版本后，确认 clone 中没有手工改动：

```bash
cd "$HOME/ai-skills/omics-method-research-skills"
git status --short
git pull --ff-only
python3 scripts/validate_repo.py
python3 install_codex.py --profile all --update --dry-run
python3 install_codex.py --profile all --update
python3 install_codex.py --check
```

有本地修改时先保留修改，不要使用 `reset --hard`。对已安装入口的手工编辑也会使更新停止。
`--update` 是增量添加与更新，不会偷偷删除之前选择的入口。
要锁定版本，使用实际已发布的 tag 或 commit，例如 `git checkout v0.2.1`；
该 tag 只有发布步骤成功后才存在，打包文件不等于远端已经有此 tag。

## 5. npx / $skill-installer 的独立校验

第三方安装完成后，在完整 clone 中运行：

```bash
python3 scripts/check_installed.py --dest "$HOME/.agents/skills"
```

这个命令与本发行版文件哈希比较，并检查依赖。
它不会将第三方安装“接管”为自带安装器管理的安装；不要随后混用 `--update`。
只安装 `omics-ot` 却没有 `omics-research` 时，校验应当失败。

## 6. Codex 加载验收

新开会话或重启未刷新技能的客户端，发送：

```text
$omics-research
只做加载验收，不安装依赖或运行科研实验。
实际读取本技能、library/GUIDE.md，以及原编号 21、25、26 的 GUIDE.md。
列出真实读取路径，分别指出独立重复、UOT质量、CFM路径的一个检查点。
区分包内历史结果、本次文件检查和本次实际执行。
```

观察实际文件读取记录；不要以口头“加载成功”代替证据。
`$omics-ot` 等写在 Codex 对话中，不要作为终端 shell 命令。

## 7. 可选插件分发

仓库另带 `plugin.json`、兼容 `.codex-plugin/plugin.json` 和本地 marketplace 描述。
这是按照查阅的官方格式补充的兼容资产，**未在 Codex 插件运行时执行验收**。
使用支持 marketplace 的客户端，可按官方文档添加真实发布后的仓库，例如：

```bash
codex plugin marketplace add OWNER/omics-method-research-skills
```

添加目录不等于已经完成插件安装和启用；后续按实际客户端的插件界面操作。
不要同时启用相同插件与同名本地 skill 入口，以免重复。
无需 MCP、外部账号依赖或生命周期 hooks；这些纯技能文件不会自动部署远端服务。
