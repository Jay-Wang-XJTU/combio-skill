---
name: 03-data-contract-and-feasibility
description: 找数据、下载、合并批次或设计 train/test 前。
version: 0.2.0
status: literature-derived-draft
---

# 数据契约、覆盖与可行性

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
找数据、下载、合并批次或设计 train/test 前。

## 必要输入
表达与模态文件；患者/动物、样本、切片、FOV、平台、阶段、随访和标签信息。

## 操作步骤
1. 建立 patient→sample→slide→FOV→cell/spot 的层级标识；保留原始 ID 与变换记录。
2. 区分原始测量、归一化值、插补表达、推断坐标及参考标签。
3. 列出设计混杂：例如所有 early 在平台 A、advanced 在 B；写明不可单独估计的效应。
4. 审计基因 panel/同源映射/计数含义/空间单位/spot 混合/缺失模态。
5. 为每个主张分配开发、比较、独立验证和生物学应用数据，记录访问限制。

## 条件分支
无患者 ID 时不能完成新患者泛化协议；无 domain 真值可做其他评价，但不把自生成簇视作真值。

## 验收条件
输入语义可追溯，独立重复数量已知，主张与数据覆盖一致。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
标记不能判断的字段；降低目标或补元数据；不悄悄将缺失病理当阴性。

## 输出产物
data_manifest.tsv；data_contract.yaml；confounding_report.md。

## 来源与解释范围
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [T2 · scArches](../../papers/T2_scArches.md)
- [P4 · ENVI / COVET](../../papers/P4_ENVI_COVET.md)
- [J3 · DeepTalk](../../papers/J3_DeepTalk.md)

## 行为测试入口
测试编号：E04, E05。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

数据契约新增处理单位、donor层级、坐标单位与测量/分割版本。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
