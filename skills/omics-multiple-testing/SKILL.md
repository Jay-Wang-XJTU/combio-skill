---
name: "omics-multiple-testing"
description: "报告显著gene/program/LR/niche、挑选driver、先聚类/拟合pseudotime再检验时。"
---

# 多重检验与选择后推断

这是 Omics GitHub 分发版 0.2.1 的技能入口；科研知识版本仍为 0.2.0。

## 依赖检查

必须在同一技能根目录安装 `omics-research`。先检查上述相对路径；缺失时停止，说明需要同时安装总入口。不要猜测知识内容，也不要未经授权联网补装。

## 读取与执行
1. 本文件中的相对路径以**本 SKILL.md 所在目录**为基准，不是项目当前工作目录。通过下面的实际文件路径定位资料库，不要在用户项目中猜测同名文件。
2. 首次使用本库时读取 [README](../omics-research/library/README.md)、[科研约束](../omics-research/library/AGENTS.md)、[验证边界](../omics-research/library/coverage_gaps.md)。这是按需读取的库约束，不是替换用户项目 AGENTS.md。
3. 读取并执行 [当前完整技能](../omics-research/library/skills/22-multiple-testing-and-selective-inference/GUIDE.md)。随后出现的相对链接以**被读取的原文件目录**为准；保留其输入、分支、验收及失败处理。
4. 按当前问题只读必要的知识章、引用、模板和交叉技能。未安装某个快捷入口时，仍可通过共享库中的 skills/ 对应文件继续工作。不要一次读取全部论文、Notebook 或历史结果。
5. 科研技能先产生与当前项目相关的判断/方案；需要执行时另核对现有环境与授权。不因加载技能而自动安装依赖、下载数据、启动训练、上传数据或触碰无关文件。
6. 默认把本次产物放在用户项目内的 docs/research/ 或用户指定目录。不要覆盖共享库的 results/ 或历史证据。需要重跑教育性实验时先复制到项目工作目录。
7. 报告本次实际读取的技能与资料路径、执行过的命令、判断及证据边界。文献事实、综合建议、计划、历史数值结果与本次执行分开；安装检查不是原论文复现。
