---
name: 21-independent-replicates-and-resampling
description: 设计患者泛化、单细胞/空间差异检验、模型性能误差条或bootstrap时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 独立重复、分层切分与重采样

## 触发条件
设计患者泛化、单细胞/空间差异检验、模型性能误差条或bootstrap时。

## 必要输入
原始counts；donor/sample/slide/FOV/cell/niche层级；处理分配；配对关系；预测目标与推断总体。

## 执行步骤
1. 在分析卡中分别指定观测、表征、实验分配、独立推断与泛化单位；以每个单位计数，禁止用seed数充当donor数。
2. 先按目标设计group holdout及nested调参；所有依赖训练的预处理、参考、图和参数都接受泄漏审计，区分联合整合和新患者预测。
3. 表达DS时选择donor×预定义cell type的raw-count聚合或适配层级模型；丰度DA另定义组成目标；缺失细胞群不自动补零。
4. 设计矩阵检查full rank与残差自由度；配对与不配对分支不同，避免condition与donor固定效应完全共线。
5. 按合法独立单位或随机化块置换/重采样，保留邻域重叠；记录零假设、交换集合及B的分辨率。
6. 输出donor级效应、区间和leave-one-donor敏感性；运行pseudoreplication反例后解释它只证明指定生成机制。

## 条件分支
只有一位donor/组：描述或补样本；有配对：pair内合法交换；只有空间随机标记零假设：不把结果解释为患者效应；高维生成任务：依据inductive/transductive协议明确holdout信息。

## 验收条件
独立单位、split与检验零假设一致；矩阵可识别；区间没有把细胞、fold、seed当独立患者。

## 失败处理
泄漏则重做全部受影响分析；独立重复不足则收缩推断，不靠增加细胞数量或BY修复。

## 输出产物
statistical_analysis_plan.yaml；unit_counts；split_manifest；design_rank；effect_table。

## 知识与证据
先读[对应知识章](../../knowledge/02_statistics.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G01, G02, G03, G06, G34。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_independent_group_guard`, `test_pseudobulk_preserves_count_sum`, `independent_replicates.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
