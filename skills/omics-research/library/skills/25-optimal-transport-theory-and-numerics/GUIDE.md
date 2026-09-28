---
name: 25-optimal-transport-theory-and-numerics
description: 用OT做时间对应、整合、空间匹配或作为FM配对时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# OT/UOT理论、数值与质量语义

## 触发条件
用OT做时间对应、整合、空间匹配或作为FM配对时。

## 必要输入
支持点语义；质量a/b和总体；成本各项/尺度；正则epsilon/rho/reference；约束与稀疏支持。

## 执行步骤
1. 写出完整优化目标，区分balanced、UOT、partial与semi-relaxed；确认质量是否有生物学数量含义。
2. 规定成本可比性、单位和prior来源；跨患者坐标不可直接对齐时禁止把其欧氏距离静默加入。
3. 显式指定KL参考测度和版本；报告linear与total不同返回量，避免迁移默认值改变科学问题。
4. 核对log-domain更新、支持裁剪、收敛残差和质量；用单点解析、LP/独立优化器做小规模数值检验。
5. 做epsilon、rho、cost尺度、reference及minibatch/近似敏感性；GW类另审计非凸初始化。
6. 输出实际行列边际与未匹配质量；连接FM前重新确认归一化后的训练源/目标分布。

## 条件分支
质量相等且应守恒：balanced；允许缺失但原因未知：UOT而不命名死亡；只保留部分固定质量：partial另建约束；异构空间：考虑GW但不默认可识别。

## 验收条件
目标函数和源码约定一致；数值已收敛；解释不超过成本/权重/质量证据；FM输入边际明确。

## 失败处理
不收敛报错而非静默输出；cost平移/缩放需重新核查；不能把行归一后的矩阵仍宣称保持原UOT边际。

## 输出产物
ot_config.yaml；cost_contract；solver_diagnostics；coupling/marginal_summary；sensitivity。

## 知识与证据
先读[对应知识章](../../knowledge/05_ot.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G15, G16, G17, G18。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_uot_against_independent_optimizer`, `test_uot_reference_changes_plan`, `optimal_transport.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
