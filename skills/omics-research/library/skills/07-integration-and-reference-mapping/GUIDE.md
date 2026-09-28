---
name: 07-integration-and-reference-mapping
description: 跨样本、患者、平台整合或将新样本映射到 atlas 时。
version: 0.2.0
status: literature-derived-draft
---

# 整合、参考映射与配准分轨

这是跨文献综合的操作建议（S/P），不是任一论文逐字规定。未通过真实项目行为验收。执行前查看 [阅读覆盖](../../references/READING_COVERAGE.md)。

## 触发条件
跨样本、患者、平台整合或将新样本映射到 atlas 时。

## 必要输入
需去除/保留的变量；训练/适配范围；参考覆盖；是否有解剖对应。

## 操作步骤
1. 分别定义联合整合、参考映射、物理配准和时间对应，不共用模糊“alignment”。
2. 列出必须保留的状态轴，特别是疾病阶段和样本特有群体。
3. 若要未见患者泛化，在全部数据依赖步骤前设定分组切分；联合分析则明确 transductive。
4. 报告同类内 batch mixing 与状态/稀有群体保留；类别之外连续信号单独评价。
5. 新状态缺乏参考时允许 unknown/低置信输出，并量化适配造成的参考漂移。

## 条件分支
阶段与批次完全混杂时，不声称算法单独分离了二者；独立患者无空间同源结构时不强制配准。

## 验收条件
去批次与保生物学均有证据，任务协议和部署假设一致。

定量阈值必须在具体项目中结合基线、噪声和主张事先设定。本 skill 不提供跨任务通用合格分数。

## 失败处理
降低整合强度或改为分层建模；补足设计；不要把所有样本混匀当唯一成功标准。

## 输出产物
integration_protocol.yaml；batch_biology_report.md；unknown_state_report.md。

## 来源与解释范围
- [T2 · scArches](../../papers/T2_scArches.md)
- [T6 · scIB integration benchmark](../../papers/T6_scIB_integration_benchmark.md)
- [Y3 · SPIRAL](../../papers/Y3_SPIRAL.md)
- [C3 · stClinic](../../papers/C3_stClinic.md)

## 行为测试入口
测试编号：E04, E08, E10。见 [评测案例](../../evaluations/cases.json)。状态：未运行；不得报告本技能已通过真实案例验证。

## v0.2 强制补充路由

跨患者inductive验证和joint integration不同；阶段/平台完全混杂不能靠指标证明分离。

- [独立重复、分层切分与重采样](../21-independent-replicates-and-resampling/GUIDE.md)。
- [空间测量链与上游误差审计](../24-spatial-upstream-measurement-error/GUIDE.md)。
- [分层不确定性、传播与校准](../28-uncertainty-propagation-and-calibration/GUIDE.md)。

这些规则补充原技能，而不把历史论文阅读或未运行实验重新标记为已完成。
