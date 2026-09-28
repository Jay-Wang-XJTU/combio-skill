---
name: 28-uncertainty-propagation-and-calibration
description: 整合多个模型/测量阶段、汇报置信区间、稳健性或恶变风险分数时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 分层不确定性、传播与校准

## 触发条件
整合多个模型/测量阶段、汇报置信区间、稳健性或恶变风险分数时。

## 必要输入
目标输出与尺度；donor/测量/算法/参数/结构不确定性；误差来源模型；重采样机制；独立真值。

## 执行步骤
1. 按来源拆分不确定性并定义比较对象，先对齐program语义、细胞映射或组织区域。
2. 以独立生物单位为外层，测量模型为内层，按任务选择固定模型评估或全流程重拟合。
3. 保留表达与几何等耦合扰动，检查来源之间及模块之间的交互；不能把所有runs视作独立样本。
4. 若只使用主观noise scenarios，则命名stress/sensitivity；有概率模型才讨论后验；有重复抽样保证才称置信区间。
5. 概率预测用目标结局检验校准与覆盖；未有随访时流向/晚期相似度不命名未来恶变概率。
6. 把稳定证据限定到相应task/program/区域；对不稳部分定位失败来源而非整项全肯定或全否定。

## 条件分支
有校准测量模型：抽样传播并检验覆盖；仅多算法分歧：报告敏感性；donor过少：不以细胞bootstrap充数；生存终点：转专门删失与时间校准流程。

## 验收条件
区间与其随机机制一致；结论与稳定对象匹配；概率的目标和验证总体清楚。

## 失败处理
发现错误覆盖或方向不稳则降低主张、聚合尺度或补证据；不将seed标准差包装为总不确定性。

## 输出产物
uncertainty_plan.yaml；layered_sensitivity；calibration_report；claim_scope_update。

## 知识与证据
先读[对应知识章](../../knowledge/07_uncertainty.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G02, G08, G12, G16, G24, G32。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`spatial_measurement.json`, `causal_identification.json`, `optimal_transport.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
