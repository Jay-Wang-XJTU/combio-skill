---
name: 13-information-matched-benchmarking
description: 比较方法、组织 benchmark 或声明性能优越时。
version: 0.2.0
status: literature-derived-draft
---

# 信息匹配与端到端 benchmark

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
比较方法、组织 benchmark 或声明性能优越时。

## 必要输入
任务、数据、标签、各方法输入/输出约束、计算预算。

## 操作步骤
1. 分两轨：相同信息的表示/算法比较；完整推荐流程的实际使用比较。
2. 披露标签、病理、参考、先验、已知 K、外部预训练和适配步骤。
3. 在语义兼容前提下控制预处理；不得把 count model 强行喂 scaled data。
4. 固定下游评价器比较表示，并另报各方法完整流程；输出图/latent/矩阵要用适配指标。
5. 多目标报告效应量、样本层级不确定性、资源和失败；调参仅用允许的数据。

## 条件分支
无可信 domain 标签时不计算伪真值准确率；已知 K 与未知 K 分开；不同任务不硬排综合榜。

## 验收条件
所有主要优势均对应同任务、可比较信息和可追溯配置；不把单个权重总分当真理。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
拆分比较组、补强简单基线或重新设计标签；不得隐去失败运行。

## 输出产物
benchmark_protocol.yaml；baseline_manifest.tsv；metric_contract.tsv。

## 来源与解释范围
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [Y4 · Spatial clustering benchmark](../../papers/Y4_Spatial_clustering_benchmark.md)
- [Y2 · MENDER](../../papers/Y2_MENDER.md)
- [J1 · DeepST](../../papers/J1_DeepST.md)

## 行为测试入口
测试编号：E03, E07, E17。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

信息匹配轨道、原标签K与完整benchmark family必须记录。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
