---
name: 15-statistical-and-clinical-validation
description: 患者分期、生存、治疗响应或样本差异分析时。
version: 0.2.0
status: literature-derived-draft
---

# 统计单位与临床验证协议

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
患者分期、生存、治疗响应或样本差异分析时。

## 必要输入
患者/切片层级；结局定义；事件/删失；协变量；训练与验证范围。

## 操作步骤
1. 以主张对应的独立单位组织切分和不确定性；细胞数不能替代患者数。
2. 患者分组外层评估，调参/特征选择/预处理适配限于协议允许范围。
3. 比较已有临床变量、组成和简单聚合基线；检查分期/平台/治疗混杂。
4. 明确随访起点和删失；风险分数的判别、校准、迁移及关联分开报告。
5. 样本级 embedding 聚合若依赖 UMAP 坐标，另比较原始高维表征和多次投影稳定性。

## 条件分支
样本少或事件少时用更简单模型和探索性表述；横截面阶段分类不自动等于未来恶变预测。

## 验收条件
验证单位、预测时间点与部署场景一致，且未用测试患者结果选择模型。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
收缩临床主张；补验证队列或调整设计；不要把重复切片当独立患者。

## 输出产物
clinical_analysis_plan.md；patient_split_manifest.tsv；confounder_report.md。

## 来源与解释范围
- [C3 · stClinic](../../papers/C3_stClinic.md)
- [P3 · Spectra](../../papers/P3_Spectra.md)
- [P2 · SEACells](../../papers/P2_SEACells.md)
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)

## 行为测试入口
测试编号：E04, E18。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

先定义独立单位/family/识别假设，再决定统计检验和校准。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [多重检验与选择后推断](../22-multiple-testing-and-selective-inference/GUIDE.md)。
- [因果识别、干预与机制证据](../23-causal-identification-and-perturbations/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
