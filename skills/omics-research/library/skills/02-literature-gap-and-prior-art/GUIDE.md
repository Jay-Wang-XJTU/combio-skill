---
name: 02-literature-gap-and-prior-art
description: 声称创新、选 baseline 或命名新任务前。
version: 0.2.0
status: literature-derived-draft
---

# 研究缺口与先例核查

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
声称创新、选 baseline 或命名新任务前。

## 必要输入
候选贡献；代表论文、原始出版页、相关代码版本。

## 操作步骤
1. 先核验作者与论文归属，记录 online year、issue year 和更正。
2. 建立任务×输入信息×分析尺度×假设×输出×验证的对比矩阵。
3. 作者自述的缺口标为待核查，阅读最接近工作的原始定义。
4. 分别判断是新问题、新表示、新假设、新求解、新规模或新证据，而非仅换架构。
5. 记录读到的确切章节；没有取得 SI/代码时，不填写确定的实现细节。

## 条件分支
已有方法任务不相同则不直接排性能榜；同任务但多用标签/图像的，转入信息匹配比较。

## 验收条件
每项创新都有最近先例和可区分实验；不同贡献类型不互相替代。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
调整定位或补读；冲突未解决时保留并列解释，不拼接成统一事实。

## 输出产物
prior_art_matrix.tsv；带读取层级的 paper_registry.json。

## 来源与解释范围
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [Y4 · Spatial clustering benchmark](../../papers/Y4_Spatial_clustering_benchmark.md)
- [Y2 · MENDER](../../papers/Y2_MENDER.md)

## 行为测试入口
测试编号：E03。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

以实际读取层级引用来源；当前main不能自动代表发表版。

- [补充材料到源码与原图复现](../27-supplement-to-code-reproduction/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
