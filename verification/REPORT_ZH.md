# GitHub 分发验收报告

分发版本 **0.2.1**；科研知识版本 **0.2.0**。

## 本轮实际执行

在 Linux / Python 3.13.5 / git version 2.47.3 环境运行：

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

**30 项部署测试全部通过，无失败、无跳过。**原始日志见 deployment_tests.log，结构化结果见 test_results.json。

覆盖：29 个入口发现、133 个共享文件及哈希、依赖链接、全量/分类/单项安装、只装总路由、
项目级安装、dry-run 无写入、幂等、增量更新与备份、同名冲突保护、手工修改保护、
符号链接/不安全清单拒绝、安装锁、旧版迁移、失败回滚、可复现 ZIP、发布计划无写入、
以及从**本地临时 Git 仓库干净 clone 后**执行安装。

检查了公共入口及共享库中的 Markdown 相对链接，保留的历史版本目录不计入链接验收。
默认安装器只用 Python 标准库。

发现并修复：paper_registry.tsv 原有 CRLF 在 Git 提交/检出时会被规范化，导致哈希不一致。
本发行版显式统一 LF，并在 provenance/library_transform.json 中保存转换前后哈希。
科研正文未扩充为新的结果；内部 SKILL.md→GUIDE.md 的改名用于避免重复注册。

## 没有执行，不能声称完成

- 真实 GitHub 身份认证、目标仓库创建、源码推送或 Release 附件上传。
- 从用户真实 GitHub 仓库下载、远端服务器部署、Codex CLI/IDE 实际调用及自动路由。
- npx CLI 端到端安装；当前环境 npm 元信息查询超时。相关命令仅经上游文档/源码核对。
- 可选 plugin/marketplace 的运行时加载；目前只做清单 JSON 与路径一致性检查。
- Windows/WSL 运行时测试。
- 重新运行原包 64 项科研测试、6 个 Notebook 或任何原论文数据复现。

技能库中的历史结果仍属于原来一轮工作，不能视为本轮重新执行。
隐私/令牌扫描只是有限模式检查，不保证已经识别所有敏感信息。公开发布前仍须人工审查。

## 上传状态

打包时没有已连接的 GitHub 写入工具，也未获知目标 OWNER/REPO 和可见性。
因此本交付是**可发布的源码与 ZIP**，不是“已经发布到 GitHub”的确认。
