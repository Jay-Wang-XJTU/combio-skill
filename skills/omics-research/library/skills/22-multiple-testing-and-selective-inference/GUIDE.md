---
name: 22-multiple-testing-and-selective-inference
description: 报告显著gene/program/LR/niche、挑选driver、先聚类/拟合pseudotime再检验时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 多重检验与选择后推断

## 触发条件
报告显著gene/program/LR/niche、挑选driver、先聚类/拟合pseudotime再检验时。

## 必要输入
完整待检验集合；每个原始p值的生成方法；筛选时间线；先验/标签来源；零假设和声明层级。

## 执行步骤
1. 判断输入是有效频率p值还是后验概率/Bayes factor/score；后几者不能直接交给BH。
2. 在看结果前定义family及筛选规则，包括gene×cell type×comparison；多层family需要相应的层级控制方案。
3. 先审查伪重复、模型拟合、可交换性及选择后有效性，再按依赖假设选择BH/BY或其他有保证方法。
4. 追踪latent/cluster/program构建与测试是否用同一信息；冻结模型或分患者并不总能解除对同一待测gene的循环。
5. 需要count splitting时先核对Poisson/NB假设与参数估计；不要把分子拆分当作新患者。
6. 保留完整p/q/effect表、过滤原因、Monte Carlo分辨率及确认性/探索性标记；运行selection反例。

## 条件分支
输入是后验量：使用对应后验决策框架或另做有效频率检验；任意依赖且p有效：可考虑BY并报告保守性；选择偏差未解决：探索性展示或专门选择性推断。

## 验收条件
family、p值有效性与依赖条件可追溯；全表可审计；报告效应与区间，而非只看q<0.05。

## 失败处理
不能用BY替代有效性；不能筛到显著后只对小集合校正；需要独立验证时不随意重定义阈值。

## 输出产物
hypothesis_family.yaml；all_tests.tsv；selection_trace；multiplicity_report。

## 知识与证据
先读[对应知识章](../../knowledge/02_statistics.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G04, G05, G06, G07, G08, G19。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_adjustments_match_statsmodels`, `test_permutation_nonzero_and_exact`, `multiple_testing.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
