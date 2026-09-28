---
name: 10-spatial-mapping-and-imputation
description: 用 scRNA 补空间基因、spot 反卷积、推断单细胞空间上下文时。
version: 0.2.0
status: literature-derived-draft
---

# 空间映射、插补与误差传递

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
用 scRNA 补空间基因、spot 反卷积、推断单细胞空间上下文时。

## 必要输入
测量面板；参考；分辨率；已测坐标和推断位置；下游任务。

## 操作步骤
1. 保存 observed/imputed 标签与原始计数，禁止覆盖真实测量而无记录。
2. 区分共享基因重建、未测基因预测、细胞组成、环境预测和唯一坐标恢复。
3. 做基因留出检验预测，再按独立样本/参考留出检验迁移；二者互不替代。
4. 检查参考缺失细胞状态、相近表达不同环境、spot 混合和 panel 偏差。
5. 对映射和插补不确定性重采样，重跑关键下游互作或风险结论。

## 条件分支
表达不能唯一确定环境时报告多个可能环境或不确定性；只有 spot 测量时不能直接称恢复了实测细胞位置。

## 验收条件
每项输出都标明测量/预测及分辨率；下游结论在合理上游扰动下仍有支持。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
缩小预测范围，恢复参考覆盖检查；限制为环境倾向而非精确定位。

## 输出产物
imputation_validation.md；provenance_layers.yaml；uncertainty_propagation.md。

## 来源与解释范围
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [J3 · DeepTalk](../../papers/J3_DeepTalk.md)
- [T2 · scArches](../../papers/T2_scArches.md)

## 行为测试入口
测试编号：E05, E14。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

插补与空间位置可能都是模型推断；分别验证，避免使用同一参考循环证明。

- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
