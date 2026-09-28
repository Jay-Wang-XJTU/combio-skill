---
name: 04-analysis-unit-and-representation
description: 选择 cell/metacell/niche 表示，或要证明超越细胞组成时。
version: 0.2.0
status: literature-derived-draft
---

# 分析单位与多尺度表示

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
选择 cell/metacell/niche 表示，或要证明超越细胞组成时。

## 必要输入
科学目标；空间单位；输入分辨率；候选邻域定义与中心锚点。

## 操作步骤
1. 明确表示代表中心细胞、邻域集合、子图还是样本；记录中心是否单独编码。
2. 分解信息：中心状态、类型/状态组成、距离分层、协变、拓扑与先验互作。
3. 同时实现与任务相关的简单比较：中心表达、组成、多尺度组成、邻域均值；必要时协变。
4. 用物理半径、kNN、k-hop 时记录实际覆盖距离和细胞数分布。
5. 重叠 niche 不作为新增患者；统计与数据切分记录共享细胞关系。

## 条件分支
目标只依赖组成时允许简单表示胜出；目标涉及状态/几何时设计组成匹配的区分测试。

## 验收条件
表示保留的信息能对应目标，尺度敏感性已报告，收益不只来自聚合粒度变化。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
调整尺度/表示或放弃无必要的复杂分支；不自动以更大 receptive field 解决一切。

## 输出产物
representation_contract.md；scale_audit.tsv；simple_baselines.yaml。

## 来源与解释范围
- [P2 · SEACells](../../papers/P2_SEACells.md)
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [Y1 · SOTIP](../../papers/Y1_SOTIP.md)
- [Y2 · MENDER](../../papers/Y2_MENDER.md)

## 行为测试入口
测试编号：E06。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

重叠niche不是独立重复；新表示的优势需与上游误差和组成基线分开。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
