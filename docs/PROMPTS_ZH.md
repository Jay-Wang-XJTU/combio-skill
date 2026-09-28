# 直接给 Codex 的提示词

## 从 GitHub 安装全部

```text
从 https://github.com/OWNER/omics-method-research-skills 安装科研技能。
先读仓库 README 和安装器，确认你实际运行在远端 Linux 还是本地。
使用 Git+Python 标准库路线，安装到当前用户 ~/.agents/skills；先 dry-run，再正式安装和 check。
检查同名目录，不覆盖人工修改；旧 v0.2 安装只能按文档校验后迁移。
不要运行论文实验、pip/conda 安装、训练或修改其他项目配置。
最后报告 commit、安装位置、29 个入口及共享库的校验结果。
```

## 用系统 skill-installer 选择 OT/FM

```text
$skill-installer
从 GitHub 仓库 OWNER/omics-method-research-skills 的同一版本安装以下目录：
skills/omics-research
skills/omics-ot
skills/omics-flow-matching
三个目录必须位于同一个技能根目录；目标是当前远端用户 ~/.agents/skills。
omics-research 是后两个入口的共享资料依赖，不能省略。
不要假设默认安装目录或自动依赖解析。先检查已有同名技能，不覆盖已有修改。
```

## Niche 表征与整合

```text
$omics-representation
$omics-integration
$omics-benchmark
读取当前项目，不假设存在未提供的阶段或标签。
审查中心表达、组成、多尺度与拓扑信息分别贡献什么；区分联合整合与未见患者映射。
输出信息匹配/端到端两个 benchmark 方案和最小证伪实验，不启动批量训练。
```

## 程序可解释性

```text
$omics-programs
$omics-robustness
$omics-multiple-testing
读取现有 encoder、decoder、mask、剪枝和跨seed结果。
分别检查重建、program语义、命运输出与driver稳定性。
先定位问题和结论边界，不直接更换整套架构。
```

## 统计及因果

```text
$omics-statistics
$omics-causal
先画出真实样本层级，明确目标量、独立重复、调整集、切分与重采样。
缺失的患者信息或因果识别条件应显式保留缺口，不用复杂模型替代。
```
