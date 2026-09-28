---
name: 20-skill-evaluation-and-versioning
description: 把文献归纳成 skill、更新规则或交给 agent 长期调用时。
version: 0.2.0
status: literature-derived-draft
---

# Skill 验收与知识更新

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
把文献归纳成 skill、更新规则或交给 agent 长期调用时。

## 必要输入
技能草稿；来源；正常案例、反例与人工验收标准。

## 操作步骤
1. 每条知识标为 F 原文事实、S 综合规则或 P 建议实验，不混写成作者结论。
2. 声明触发条件、输入、步骤、分支、验收、失败处理和产物。
3. 用正常案例、边界案例、故意错误案例测试 agent 是否作出正确研究决策。
4. 检查文献版本、作者归属、文献覆盖与未解决冲突；缺失信息应降低确定性。
5. 新证据导致修改时记录变化理由、影响的 skills、旧结论是否失效。

## 条件分支
格式 lint 通过只证明包结构一致；实际案例通过才可报告行为验收，且不等于科学结果复现。

## 验收条件
正常与反例测试都留有执行记录；未运行的测试保持 not_run。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
缩小触发范围、完善失败分支或撤回错误规则；不以增加论文数量代替验证。

## 输出产物
evaluation_results.json；CHANGELOG.md；coverage_gaps.md。

## 来源与解释范围
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [Y4 · Spatial clustering benchmark](../../papers/Y4_Spatial_clustering_benchmark.md)
- [J2 · DeepCCI](../../papers/J2_DeepCCI.md)
- [C3 · stClinic](../../papers/C3_stClinic.md)

## 行为测试入口
测试编号：E22。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

数值/结构测试、notebook执行、agent行为评测和论文复现是四类不同验证。

- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
