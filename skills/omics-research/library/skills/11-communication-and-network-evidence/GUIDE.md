---
name: 11-communication-and-network-evidence
description: LR 互作、基因网络、链接预测或通讯解释时。
version: 0.2.0
status: literature-derived-draft
---

# 通讯、网络与标签来源审计

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
LR 互作、基因网络、链接预测或通讯解释时。

## 必要输入
先验数据库版本；表达；空间信息；训练标签生成器；负例规则。

## 操作步骤
1. 区分 LR 候选、统计共现、空间接近、模型链接和功能通讯证据。
2. 逐项审计多亚基、方向、物种映射、检测率、分泌/接触作用范围。
3. 标签若来自其他工具，目标标为学习该标签规则或共识；单独记录独立实验标签。
4. 未标注链接不自动作为真实阴性；设计匹配的负例/背景并检查采样偏差。
5. 比较简单 LR 分数、原标签生成器和上下文模型；分开定位精度和互作证据。

## 条件分支
只有表达和数据库时输出候选；加入独立受体/蛋白/响应证据可提高支持，但因果主张仍需相应干预设计。

## 验收条件
主张与标签来源一致；不以同一数据库的重叠为独立验证。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
重写结论、增设外部验证或改无/弱监督目标；不伪造真阴性。

## 输出产物
label_provenance.tsv；interaction_evidence.tsv；negative_sampling.md。

## 来源与解释范围
- [J2 · DeepCCI](../../papers/J2_DeepCCI.md)
- [J3 · DeepTalk](../../papers/J3_DeepTalk.md)
- [C1 · CSN](../../papers/C1_CSN.md)
- [C2 · stKeep](../../papers/C2_stKeep.md)
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)

## 行为测试入口
测试编号：E09, E15。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

通讯标签先验、伪共表达、依赖和干预效应需分开；attention不等于因果通讯。

- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
