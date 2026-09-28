---
name: 14-robustness-and-identifiability
description: 多 seed 不一致、解释易变或准备报告稳健性时。
version: 0.2.0
status: literature-derived-draft
---

# 稳定性、可识别性与误差来源

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
多 seed 不一致、解释易变或准备报告稳健性时。

## 必要输入
多次结果；样本层级；程序语义；上游步骤和超参数。

## 操作步骤
1. 分别测优化随机性、细胞重采样、患者差异、先验扰动、panel/平台差异。
2. 按声明对象测指标：任务输出、几何、概率、program 排名、driver 集合。
3. 检查排列、旋转、缩放等模型对称性；先对齐合法自由度再比较，不能用对齐隐藏语义漂移。
4. 重跑整个关键流程以传播上游不确定性；只固定 embedding 重训头不算全流程稳健。
5. 区分观测不足、多解、优化失败和生物异质性；稳定性不能由单项指标替代。

## 条件分支
整体预测稳定但 driver 不稳定时只降低 driver 声明，不无依据否定全部模型；反向亦然。

## 验收条件
报告每层稳定性及其对相应主张的影响，无“整体稳定”含混结论。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
针对来源修复：约束/重设计、增加数据、改优化或分层解释；不盲目扩大 seed 数代替问题定位。

## 输出产物
stability_by_object.tsv；uncertainty_budget.md；failure_diagnosis.md。

## 来源与解释范围
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)
- [P2 · SEACells](../../papers/P2_SEACells.md)
- [T3 · CellRank 2](../../papers/T3_CellRank_2.md)

## 行为测试入口
测试编号：E11, E12。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

seed、donor、上游测量与结构先验四种稳健性不要合为一个结论。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
