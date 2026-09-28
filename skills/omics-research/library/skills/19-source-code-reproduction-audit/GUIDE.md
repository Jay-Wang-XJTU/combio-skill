---
name: 19-source-code-reproduction-audit
description: 移植模型、复现 baseline、确认论文实现或发布 skill 前。
version: 0.2.0
status: literature-derived-draft
---

# 论文—代码—结果三方审计

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
移植模型、复现 baseline、确认论文实现或发布 skill 前。

## 必要输入
原文与补充方法；官方仓库；论文版本/commit；数据和配置。

## 操作步骤
1. 固定源码来源和论文对应版本；记录 license 和访问限制，不混用 fork。
2. 逐项比对预处理、loss、mask、梯度流、图构造、默认参数及训练/推断路径。
3. 遇到 PDF 公式解析异常，检查原始图像与实现，不将排版损坏的公式写入代码。
4. 先跑官方最小例，再复现一个核心图/表；区分可运行、数值近似和结论复现。
5. 记录无法取得的数据、模型和依赖；当前文档新增功能不能倒推原论文已做。

## 条件分支
本知识包全部论文当前均未完成这一步；执行本 skill 后才可提高对应条目的审计等级。

## 验收条件
审计日志包含具体版本、命令、输出及差异；没有执行证据就保持未验证。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
将实现差异交由明确的选择分支处理；不要悄然修复论文而仍称原版复现。

## 输出产物
implementation_diff.tsv；reproduction_report.md；pinned_versions.json。

## 来源与解释范围
- [T1 · scVelo](../../papers/T1_scVelo.md)
- [P1 · Palantir](../../papers/P1_Palantir.md)
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)

## 行为测试入口
测试编号：E21。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

用正交证据字段取代单一“复现完成”；所有原图重跑须有输入/输出hash与日志。

- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
