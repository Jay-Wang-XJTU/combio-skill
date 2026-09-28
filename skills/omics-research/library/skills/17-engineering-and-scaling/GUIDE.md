---
name: 17-engineering-and-scaling
description: 实现新方法、HPC 批量实验或声称可扩展时。
version: 0.2.0
status: literature-derived-draft
---

# 可复现工程与规模边界

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
实现新方法、HPC 批量实验或声称可扩展时。

## 必要输入
数据规模、特征维数、图密度、目标硬件、软件约束与随机种子。

## 操作步骤
1. 先实现小数据的参考版本与形状/数值断言，再优化。
2. 显式估算所有细胞对、基因对、子图重复和距离矩阵成本，避免无意构造 dense N×N。
3. 使用配置驱动数据/模型/训练/评价，保存切分、先验和缓存的哈希。
4. 记录硬件、精度、线程、wall time、峰值内存及失败状态；不得只报成功案例。
5. 比较近似/缓存/采样优化前后的目标指标、图邻域或耦合，而非只比较 runtime。

## 条件分支
近似改变结果时报告精度—成本权衡；现有库版本不能假定与论文一致。

## 验收条件
同配置可追溯；小规模数值检查通过；规模曲线含质量与资源而非单条时间。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
优先稀疏化或近似并验正确性；不要通过省略关键评价获得虚假提速。

## 输出产物
run_manifest.json；environment_lock；scaling_report.tsv；sanity_checks.md。

## 来源与解释范围
- [Y2 · MENDER](../../papers/Y2_MENDER.md)
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [T4 · moscot](../../papers/T4_moscot.md)
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)

## 行为测试入口
测试编号：E20。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

锁版本和目标函数；记录数值收敛、近似误差与真实资源，不以代码跑通等于科学正确。

- [OT/UOT理论、数值与质量语义](../25-optimal-transport-theory-and-numerics/GUIDE.md)。
- [Flow matching配对、路径与ODE验证](../26-flow-matching-design-and-validation/GUIDE.md)。
- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
