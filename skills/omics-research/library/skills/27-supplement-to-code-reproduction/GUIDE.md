---
name: 27-supplement-to-code-reproduction
description: 把文献经验升级为具体实现、迁移算法或声称“已复现”时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# 补充材料到源码与原图复现

## 触发条件
把文献经验升级为具体实现、迁移算法或声称“已复现”时。

## 必要输入
论文/版本/更正；全部SI文件目录；软件与分析仓库；归档/commit；数据/许可；目标figure与容差。

## 执行步骤
1. 建立逐文件逐图表coverage清单，区分下载、文字阅读、页图核对和结果复现；不足处明确null。
2. 追踪claim→SI定位→函数→输入/配置→输出/指标；source data不是输入训练数据，软件仓库不等于分析仓库。
3. 锁定发表版本与依赖，保留原要求和适配patch；不随意改用户主环境。
4. 先做独立公式/函数微验证，再运行官方最小示例，再重跑指定原图，最后扩展全数据。
5. 记录实际命令、退出码、环境、输入/输出SHA256、数值与科学容差，保存失败运行。
6. 用正交证据等级标注结论；synthetic单元通过不升级成原数据复现，静态检查不升级成agent能力。

## 条件分支
SI/数据访问失败：记录具体阻塞；版本冲突：隔离环境与patch；算法必须修改：称适配版；数据受控：不上传到公共包。

## 验收条件
复现状态有真实日志和对应数据/版本支持；完整SI无隐性遗漏；结果差异可解释并保留。

## 失败处理
不虚构参数/commit/数据；不能从正文猜未读SI；未完成的实验保留为计划而不是结论。

## 输出产物
reproduction_manifest.yaml；supplement_coverage；source_audit；execution_log；figure_diff。

## 知识与证据
先读[对应知识章](../../knowledge/01_reproduction.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G19, G20, G21, G18, G25。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_posterior_probability_formula_not_a_pvalue`, `tests/test_package.py`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
