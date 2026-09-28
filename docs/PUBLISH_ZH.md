# 发布到 GitHub：源码与压缩包是两件事

**可安装内容必须作为源码树出现在仓库中**：根目录应直接有 README.md、skills/、scripts/。
只把 ZIP 上传到仓库首页不能让目录型 skill 安装器自动识别内部技能。
完整 ZIP 可作为 GitHub Release 附件发布；它是额外下载渠道，不替代源码。

## 1. 发布前需要用户确定的事项

选择真实的 `OWNER/REPO`、新建或已有仓库，以及 `private` 或 `public`。
建议首次先用私有仓库验收。公开之前自行检查研究材料、第三方许可和残留个人路径。
本包没有擅自添加 MIT/Apache 等许可证或虚构权利人，见 LICENSE_AND_ATTRIBUTION.md。

在自己有授权的机器配置 Git 和 GitHub CLI：

```bash
git --version
gh --version
gh auth login
gh auth status
```

若 Git 尚无提交身份，配置真实信息（可使用个人 GitHub 的 noreply 邮箱）：

```bash
git config --global user.name "YOUR_GIT_NAME"
git config --global user.email "YOUR_VERIFIED_OR_NOREPLY_EMAIL"
```

此配置会影响该用户后续 Git 提交；已有正确配置不要重设。
不要把 PAT、SSH 私钥、浏览器 cookie 或 Codex auth.json 上传到仓库或粘贴到聊天。
本脚本不会索要/显示认证令牌。

## 2. 新建仓库：使用发布助手

解压本包，进入含 README.md 的 `omics-method-research-skills` 文件夹。

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v

# 预览，不联网、不修改仓库
python3 scripts/publish_github.py \
  --repo OWNER/omics-method-research-skills --visibility private --release

# 经你审查后正式执行：新建私有仓库、推送源码，上传 ZIP 到 Draft Release
python3 scripts/publish_github.py \
  --repo OWNER/omics-method-research-skills --visibility private --release --execute
```

公开发布须由你明确把 `private` 改成 `public`；脚本没有隐含公开默认值。
脚本只创建新仓库，发现已有仓库会停止，不会覆盖默认分支或 force push。
它把显式 `RELEASE_FILES.json` 清单中的文件复制到一个独立临时工作树后提交；
`.local/`、`.git/`、token、实际项目数据与未列入发布清单的附加文件不会被随手 `git add .` 带进去。
若更改源码，先审查并更新清单/测试，不能绕过哈希检查。

`--release` 会创建并推送 `v0.2.1` tag，并上传源码 ZIP 和 SHA256 到 **Draft Release**。
Draft 不自动公开发布，仍需到 GitHub 审查并点击 Publish release。
不带 `--release` 只推送源码。
脚本不是跨网络事务；若中途失败，仓库或 tag 可能已成功创建，检查命令输出，不要盲目重试新建。
临时工作树会保留在 `.local/publish-*`，便于检查和恢复。

## 3. 不用脚本的等价路线

先用 `python3 scripts/build_release.py` 构建附件。
在一个新的、不属于任何现有项目的目录解压本包，再执行：

```bash
git init -b main
git add README.md VERSION catalog.json SKILLS_SHA256.json RELEASE_FILES.json \
  LICENSE_AND_ATTRIBUTION.md CHANGELOG.md AGENTS.md install_codex.py \
  .gitignore .gitattributes .github .agents .codex-plugin plugin.json \
  skills scripts docs tests provenance verification
git diff --cached --stat
git commit -m "Release omics research skills distribution v0.2.1"
gh repo create OWNER/omics-method-research-skills \
  --private --source=. --remote=origin --push

git tag v0.2.1
git push origin refs/tags/v0.2.1
gh release create v0.2.1 dist/omics-method-research-skills-v0.2.1.zip \
  dist/omics-method-research-skills-v0.2.1.zip.sha256 \
  --repo OWNER/omics-method-research-skills --verify-tag --draft \
  --title "Omics research skills v0.2.1" --notes-file docs/RELEASE_NOTES.md
```

## 4. 目标仓库已经存在

不要用新建仓库助手，也不要 `push --force`。
先通过 `gh repo clone OWNER/REPO` 得到真正的远端仓库，在新分支上加入文件，检查冲突后提交 PR。

```bash
gh repo clone OWNER/REPO existing-omics-repo
cd existing-omics-repo
git switch -c add-omics-skills-v0.2.1
```

把本包源码有选择地合并进去，**保留现有 `.git`、现有 AGENTS.md/README/CI 配置，逐项解决冲突**。
不将其他实验项目目录当作发布目标，不直接覆盖同名文件。
若仓库仅用于这个技能库，推荐源码放根目录；若放子目录，安装 URL、脚本根路径与 marketplace
来源也需要按真实结构更新并复验，不应套用本文件的根目录命令。

确认变更只包含预期文件后：

```bash
git diff --stat
git add <reviewed-files>
git diff --cached --stat
git commit -m "Add omics research skills distribution"
git push -u origin add-omics-skills-v0.2.1
gh pr create --title "Add Omics research skills" --body "Add reviewed skill sources, install scripts and deployment tests."
```

`<reviewed-files>` 是待替换的说明，不是可直接粘贴执行的 shell 参数。

## 5. 只用 GitHub 网页

新建目标仓库并明确可见性，在 Code → Add file → Upload files 上传解压后的源码内容。
文件较多、包含隐藏的 `.github` / `.agents` / `.codex-plugin` 时，网页上传容易漏文件，优先 Git。
新建 Release 时把完整 ZIP 作为附件另传。
不要只上传一个 ZIP，再声称仓库支持目录型安装。

## 6. 上传后验收

在**另一个干净目录或远端机器**clone真实URL，记录commit，运行validate、安装与check，
再在真实Codex新会话中验收实际读取路径。
GitHub源码推送、Release上传、Codex文件安装与客户端加载四个状态分别记录，不相互替代。
