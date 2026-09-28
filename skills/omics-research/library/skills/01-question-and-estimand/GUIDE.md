---
name: 01-question-and-estimand
description: 提出新计算方法、项目启动或模型目标反复改变时。
version: 0.2.0
status: literature-derived-draft
---

# 科学问题与可检验目标

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
提出新计算方法、项目启动或模型目标反复改变时。

## 必要输入
生物学问题；已知数据结构；预期用户；拟声称的结论。

## 操作步骤
1. 把“更好的 embedding”改写为具体研究对象、使用场景与决策用途。
2. 分开分析单位、观测单位、独立重复单位：例如 niche、spot、患者。
3. 逐项记录可观测量、隐变量、目标量、方向先验及可证伪条件。
4. 将主张标为描述、预测或机制解释；每类对应不同验证。
5. 构造最强简单方案：若它足以回答问题，优先转为应用或限定方法改进，而非强行堆模型。

## 条件分支
数据只能支持横截面状态对应时，保留该目标并把真实时间/恶变概率列为待验证；确有独立随访再设计风险预测。

## 验收条件
每个主要主张都能指向一个可执行测试、对照和数据来源；不能只指向 UMAP。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
收缩主张、补采关键信息或改目标；不以增加网络容量替代不可识别性分析。

## 输出产物
question_card.md；claim_evidence.tsv 的初稿。

## 来源与解释范围
- [P2 · SEACells](../../papers/P2_SEACells.md)
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [T3 · CellRank 2](../../papers/T3_CellRank_2.md)
- [T4 · moscot](../../papers/T4_moscot.md)

## 行为测试入口
测试编号：E01, E02。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

先区分描述/预测/因果estimand、独立单位及可观察验证目标。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
