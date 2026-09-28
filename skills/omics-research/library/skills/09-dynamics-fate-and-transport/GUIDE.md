---
name: 09-dynamics-fate-and-transport
description: 伪时间、命运推断、跨时间 OT 或连续状态建模时。
version: 0.2.0
status: literature-derived-draft
---

# 状态动态、命运与最优传输

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
伪时间、命运推断、跨时间 OT 或连续状态建模时。

## 必要输入
真实时间/velocity/谱系/根与终态信息；采样设计；候选代价和质量约束。

## 操作步骤
1. 先记录方向来自观测还是设定；不能从无方向距离自动推出生物学时间。
2. 分开核构建、命运求解、路径可视化和 driver 关联。
3. OT 显式写明被运输对象、代价、结构代价、熵正则与边缘质量约束。
4. 用替代合理的 root、terminal、cost 和采样比例重算；检查无支撑对应与不连通分支。
5. 质量不匹配同时考虑增殖/死亡和采样/检测差异，不能直接把全部质量解释成出生死亡。

## 条件分支
只有不配对 early/late 样本时输出条件于假设的对应或轨迹候选；有真实谱系/中间时间才能做额外验证。Flow matching 的定理及实现不在本轮核读范围。

## 验收条件
方向与尺度的依据明确；关键结论不依赖唯一任意设定，或已报告其依赖。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
报告多解/不可识别部分；退回状态相似或部分对应，不将生成的路径作为实测事实。

## 输出产物
dynamics_assumptions.yaml；coupling_sensitivity.md；fate_validation.md。

## 来源与解释范围
- [T1 · scVelo](../../papers/T1_scVelo.md)
- [P1 · Palantir](../../papers/P1_Palantir.md)
- [T3 · CellRank 2](../../papers/T3_CellRank_2.md)
- [T4 · moscot](../../papers/T4_moscot.md)
- [Y1 · SOTIP](../../papers/Y1_SOTIP.md)

## 行为测试入口
测试编号：E01, E02, E13。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

使用UOT实际边际定义FM训练分布；普通概率ODE不建模质量源汇或唯一真实历史。

- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。
- [OT/UOT理论、数值与质量语义](../25-optimal-transport-theory-and-numerics/GUIDE.md)。
- [Flow matching配对、路径与ODE验证](../26-flow-matching-design-and-validation/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
