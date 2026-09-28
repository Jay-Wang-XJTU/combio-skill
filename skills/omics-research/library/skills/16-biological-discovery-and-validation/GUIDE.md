---
name: 16-biological-discovery-and-validation
description: 从计算结果提出 marker、program、driver、niche 机制时。
version: 0.2.0
status: literature-derived-draft
---

# 生物学发现与验证梯度

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
从计算结果提出 marker、program、driver、niche 机制时。

## 必要输入
候选发现；输入先验；数据来源；可用独立样本、蛋白、谱系或干预。

## 操作步骤
1. 区分恢复已知现象、发现新关联、预测新结局和解释机制。
2. 为每个发现列出至少一个竞争解释，如组成、身份、深度、组织区域或平台。
3. 独立验证优先不重复使用训练依据；保持目标问题与验证对象一致。
4. 需要机制结论时联合实验设计，写明可区分竞争解释的操纵与读出。
5. 记录阴性和不一致证据；生物学不支持时不靠更多富集图替代。

## 条件分支
方法性能主张不强制全部做湿实验；“驱动”或“通讯导致”则需要与该因果强度匹配的证据。

## 验收条件
每项结论有证据等级、适用条件和未排除的解释；候选明确标为候选。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
缩小为关联/预测结论、补充鉴别性实验或撤回局部解释。

## 输出产物
biological_claim_cards.md；validation_matrix.tsv；alternative_explanations.md。

## 来源与解释范围
- [T4 · moscot](../../papers/T4_moscot.md)
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [T5 · NicheCompass](../../papers/T5_NicheCompass.md)
- [J2 · DeepCCI](../../papers/J2_DeepCCI.md)

## 行为测试入口
测试编号：E15, E19。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

先检查发现是否超出测量伪影和先验循环，再区分描述、预测与机制验证。

- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
