---
name: 08-interpretable-program-learning
description: 基因程序 latent、masked decoder、gene-set priors 或 driver 排名时。
version: 0.2.0
status: literature-derived-draft
---

# 可解释程序、语义对齐与证据

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
基因程序 latent、masked decoder、gene-set priors 或 driver 排名时。

## 必要输入
gene sets 及来源；重叠；decoder mask；cell type；各状态参数共享方案。

## 操作步骤
1. 区分输入先验、模型定义分数、实际支持基因和外部生物学解释。
2. 列出 hard mask、soft penalty、稀疏化、共享/特异程序分别限制什么；共享 decoder 不自动证明唯一可识别。
3. 比较总重建贡献、类型内变异解释、跨状态比较和任务关联，不能互相代替。
4. 开展先验基因留出/错配先验/去身份标记分析，分辨 target 与 regulator 支持。
5. 跨 seed 比较前按模型对称性处理排列/缩放；有固定语义维度时核验语义，而非任意旋转成一致。

## 条件分支
无先验的 latent 重点评子空间/邻域；宣称 program 语义则必须在 program 层验收；driver 需额外证据。

## 验收条件
解释对象、稳定粒度和证据来源清楚；重建、排名稳定和外部支持分别报告。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
降级为程序相关表征或候选机制；检查冗余先验、不可识别、目标冲突和样本差异。

## 输出产物
program_dictionary.tsv；interpretability_audit.md；stability_by_object.tsv。

## 来源与解释范围
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [C1 · CSN](../../papers/C1_CSN.md)

## 行为测试入口
测试编号：E11, E12。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

审计program后验概率与p值的不同语义；重建、排名和跨状态语义分别检验。

- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
