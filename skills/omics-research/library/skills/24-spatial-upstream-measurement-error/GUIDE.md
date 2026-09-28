---
name: 24-spatial-upstream-measurement-error
description: 构造空间图、发现罕见混合状态/界面生态位、比较分割或推断通讯前。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 空间测量链与上游误差审计

## 触发条件
构造空间图、发现罕见混合状态/界面生态位、比较分割或推断通讯前。

## 必要输入
平台与版本；分子/spot/count/图像/边界；坐标单位和FOV；negative/background；参考与注释来源。

## 执行步骤
1. 画出本平台测量链，从检测/分割或捕获/扩散到counts、annotation、graph；区分观察与模型推断信息。
2. 检查错分配、merge/split、漏检、背景污染、面板缺失、坐标/FOV拼接及组织mask；不要统一当独立Gaussian噪声。
3. 选择与测量机制相符的校正与验证；记录算法版本，不把历史Xenium教程等同所有当前数据。
4. 检查marker优化导致的循环验证；优先用独立染色、人工核查或未参与上游建模的证据。
5. 扰动或抽样上游后重算counts、注释、邻域与下游；不同分割节点先建立映射或转到共同区域。
6. 分别报告固定模型与全流程重拟合的敏感性，并把主观stress范围与校准不确定性区分。

## 条件分支
无分子/图像：只能做可见层面的检查并记录不可见风险；Visium：反卷积不是单细胞坐标；成像分割：类型与几何误差可能相关。

## 验收条件
坐标/ID/背景契约通过；关键结论在合理上游设置下稳定或明确限定；未知误差率不伪装实测。

## 失败处理
上游伪影则回到分配/坐标/参考处理；不能只在最后embedding加噪声后宣称全面稳健。

## 输出产物
measurement_error.yaml；QC_by_sample；assignment/coordinate_audit；propagation_report。

## 知识与证据
先读[对应知识章](../../knowledge/04_spatial_error.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G11, G12, G13, G14, G28, G29, G30。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_knn_geometric_invariance`, `test_zero_contamination_identity`, `spatial_measurement.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
