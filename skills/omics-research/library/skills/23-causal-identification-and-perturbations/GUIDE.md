---
name: 23-causal-identification-and-perturbations
description: 声称driver、调控因果、反事实、干预效果或“恶变概率”时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 因果识别、干预与机制证据

## 触发条件
声称driver、调控因果、反事实、干预效果或“恶变概率”时。

## 必要输入
目标总体/单位；处理操作与时点；结局；处理前/后变量；分配与选择机制；DAG和证据。

## 执行步骤
1. 把预测、平均干预效应、个体反事实和机制解释分开；填写可实际操作的处理和对照。
2. 建立DAG并标出未测混杂、collider、mediator及selection；不把所有embedding维度盲目作为调整变量。
3. 检查一致性、可交换性、positivity、干扰/处理版本；给出识别公式，或明确为何当前不能识别。
4. 仅在识别条件支持后选择g-computation/IPW/AIPW；独立单位cross-fit，检查权重、重叠与有效样本量。
5. 扰动数据审计guide检测、编辑成功、off-target、存活和处理后选择；按真正想泛化的gene/donor/context分割。
6. 设计负对照、替代DAG与未测混杂敏感性；对OT/FM/通讯仅有模型输出时不升级成真实干预机制。

## 条件分支
有随机化：检查执行与选择；观测数据：明确调整及不可检验假设；有邻居干扰：定义暴露映射或cluster干预；不能识别：保留预测/关联任务。

## 验收条件
每个因果主张都有estimand、识别假设及匹配证据；不能仅以拟合优度过关。

## 失败处理
发现collider或处理后变量则重新设计；overlap差则报告目标变化；不通过加大网络修复缺失识别。

## 输出产物
causal_estimand.yaml；DAG_edge_evidence；identification_note；overlap_and_sensitivity_report。

## 知识与证据
先读[对应知识章](../../knowledge/03_causal.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G09, G10, G31, G32, G33, G35。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_aipw_randomized_linear_known_effect`, `causal_identification.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
