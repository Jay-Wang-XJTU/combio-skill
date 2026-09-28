---
name: 12-minimum-falsification-and-simulation
description: 大规模训练前，或要判断新增模块是否必要时。
version: 0.2.0
status: literature-derived-draft
---

# 最小证伪实验与受控模拟

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
大规模训练前，或要判断新增模块是否必要时。

## 必要输入
核心机制假说；预期成功/失败条件；简单基线。

## 操作步骤
1. 一次只测试最核心的新能力，并给出能够推翻它的结果。
2. 用表达状态、组成、空间排列、技术噪声等独立因素构造对照。
3. 同时模拟假设成立和被破坏的情形；避免只按自家模型生成数据。
4. 对拓扑或通讯置换保持与假说无关的条件，如度、组成、检测率或空间区域。
5. 预先写明继续、简化、重构与暂不支持的判断标准；阈值绑定项目而非论文默认值。

## 条件分支
算法只需离散分区和需要连续梯度时采用不同反例；有真实干预或谱系数据优先补充而非只模拟。

## 验收条件
简单基线和破坏性对照可运行，且检查确实针对目标机制，不只是优化 loss。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
停止扩展无效模块；修正假设或数据要求；记录失败而非只保留最好 seed。

## 输出产物
minimal_experiment.yaml；simulation_factorial.tsv；go_no_go.md。

## 来源与解释范围
- [Y1 · SOTIP](../../papers/Y1_SOTIP.md)
- [Y3 · SPIRAL](../../papers/Y3_SPIRAL.md)
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [T3 · CellRank 2](../../papers/T3_CellRank_2.md)

## 行为测试入口
测试编号：E06, E16。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

使用独立数值oracle与可证伪反例；toy通过只支持toy的输入机制。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [OT/UOT理论、数值与质量语义](../25-optimal-transport-theory-and-numerics/GUIDE.md)。
- [Flow matching配对、路径与ODE验证](../26-flow-matching-design-and-validation/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
