---
name: 06-graph-and-message-passing-design
description: 构造 GNN、跨切片图、异构图或子图编码器时。
version: 0.2.0
status: literature-derived-draft
---

# 图语义、采样和信息传播

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
构造 GNN、跨切片图、异构图或子图编码器时。

## 必要输入
节点/边候选；坐标；表达表示；先验；训练和推断访问范围。

## 操作步骤
1. 逐种边标注来源：物理邻接、表达相似、跨样本匹配、基因关联或候选 LR；不可混称通讯边。
2. 写明有向性、权重、归一化、自环、边类型与不同层参数共享。
3. 审计子图重叠、中心标记、边界截断、负采样、共享节点的多个表示如何使用。
4. 比较无图/空间图/表达图/联合图，并检查消息传播是否消除目标差异。
5. 动态删边记录每轮增删及其生物学区域；跨切片边不是物理距离边。

## 条件分支
任务要离散分区可测试边剪枝；任务要连续过渡必须检查桥接保留。归纳部署不得无说明访问测试标签或训练时不可得图结构。

## 验收条件
每类边有可追溯语义和至少一项针对性反例；attention 不直接输出为物理通讯强度。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
缩减边型、修复标签泄漏、保留连续桥；不能只用更清晰 UMAP 判断图正确。

## 输出产物
graph_contract.yaml；edge_audit.tsv；sampling_design.md。

## 来源与解释范围
- [C2 · stKeep](../../papers/C2_stKeep.md)
- [C3 · stClinic](../../papers/C3_stClinic.md)
- [J3 · DeepTalk](../../papers/J3_DeepTalk.md)
- [Y3 · SPIRAL](../../papers/Y3_SPIRAL.md)

## 行为测试入口
测试编号：E08, E09。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

先排除跨FOV坐标错连与holdout泄漏；注意邻域重叠造成依赖。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
