---
name: 05-observation-model-and-preprocessing
description: 选 NB/Poisson/MSE、组合模态、训练生成模型或移植基线时。
version: 0.2.0
status: literature-derived-draft
---

# 观测模型与预处理兼容性

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
选 NB/Poisson/MSE、组合模态、训练生成模型或移植基线时。

## 必要输入
每个输入层的数值语义、变换、采样技术、训练目标。

## 操作步骤
1. 给矩阵标注 raw counts、log-normalized、scaled、proportions、binary 或 imputed。
2. 为每个解码目标写出支持集和尺度；计数似然不直接重建含负数的标准化矩阵。
3. 逐层列出编码输入与重建目标，两者可不同但须有理由。
4. 记录库大小、检测率、离散度及技术协变量如何进入模型。
5. 以按表达量/检测率分层的重建误差或预测检查评价，而不是只报总 loss。

## 条件分支
平台有不同观测过程时允许不同 likelihood；不得把某论文的默认分布推广为所有平台的真机制。

## 验收条件
数据支持集、loss 与实现一致；不存在靠全零预测获得误导性高分的单一评价。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
修复数据流或重建目标；检查 collapse、库大小支配、权重尺度，不能靠删零掩盖问题。

## 输出产物
tensor_schema.tsv；likelihood_audit.md；reconstruction_diagnostics.md。

## 来源与解释范围
- [T1 · scVelo](../../papers/T1_scVelo.md)
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)

## 行为测试入口
测试编号：E07。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

原始count、归一化输入、插补值必须区分；分割混合误差不等于NB过度离散。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
