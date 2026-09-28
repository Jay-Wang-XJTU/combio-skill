---
name: 18-claim-evidence-and-paper-design
description: 组织 Results、选主图、写摘要或回应审稿时。
version: 0.2.0
status: literature-derived-draft
---

# 主张—证据与论文组织

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
组织 Results、选主图、写摘要或回应审稿时。

## 必要输入
主张清单；全部实验；失败/稳健性；来源和脚本。

## 操作步骤
1. 每个主张对应数据、实验、对照、指标、统计单位和限定条件。
2. 图的顺序按问题—方法—能力—生物学—边界组织，而不是按网络模块个数。
3. 禁止把 UMAP、富集、预测、注意力同时作为同一机制的相互独立证据而不检查共享来源。
4. 检查摘要结论是否超过最强独立证据；重复标签生成过程不算新增真值。
5. 审稿材料仅作为具体质疑案例；未获取的材料不推测内容，发表不等于无局限。

## 条件分支
证据只支持局部或特定数据时在结论中保留范围；未完成实验列为缺口而非填补结果。

## 验收条件
所有主要文字有可追踪产物和适当限定，不存在无实验支撑的关键 claim。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
删改结论、补针对实验或降级证据等级，不能只改措辞掩盖缺口。

## 输出产物
claim_evidence.tsv；figure_plan.md；limitations.md。

## 来源与解释范围
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [T4 · moscot](../../papers/T4_moscot.md)
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [C3 · stClinic](../../papers/C3_stClinic.md)

## 行为测试入口
测试编号：E19。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

证据不足时缩小具体claim；不把所有失败汇总成空泛limitation。

- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。
- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
