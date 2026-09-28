---
name: 26-flow-matching-design-and-validation
description: 从状态分布学习向量场、连接UOT与FM、解释轨迹/箭头/命运时。
version: 0.2.0
status: literature-derived-with-scoped-numerical-checks
---

# Flow matching配对、路径与ODE验证

## 触发条件
从状态分布学习向量场、连接UOT与FM、解释轨迹/箭头/命运时。

## 必要输入
端点及split；coupling/采样权重；time单位；path/noise schedule及导数；网络；ODE；验证真值。

## 执行步骤
1. 分开endpoint coupling、conditional path和ODE solver；CondOTProbPath本身不完成端点OT。
2. 推导x_t与dx_t并验证time广播；改变schedule/noise后重新求导，不照抄x1-x0。
3. 校验UOT归一化后源目标边际；质量源汇需要额外机制，普通概率ODE不自动处理。
4. 以独立验证速度误差＋ODE积分端点误差双重检查训练；核查设备、eval/no_grad及积分方向。
5. 做solver步数、coupling、batch size、noise、prior敏感性；保留高维场而非只解释UMAP箭头。
6. 用独立中间时间/谱系/干预验证路径；区别确定性轨线、隐变量引起的一对多和模型条件平均。

## 条件分支
只有两端：描述模型对应而非唯一真实历史；需增长：加显式质量模型或只分析匹配质量；需同状态随机分支：额外随机变量/过程并另验证；真实时间未知：速度只用归一化单位。

## 验收条件
路径/导数/采样正确且ODE端点过关；质量与方向解释诚实；不把low loss或漂亮箭头当生物学机制。

## 失败处理
端点失败先查coupling/schedule/normalization/solver；无法验证中间路径则收缩叙述，不加网络替代证据。

## 输出产物
fm_config.yaml；path_derivation；training_and_solver_report；biological_validation_matrix。

## 知识与证据
先读[对应知识章](../../knowledge/06_flow_matching.md)，再查[来源与真实阅读范围](../../references/GAP_SOURCES.md)。来源：G22, G23, G24, G25, G26, G27。

## 可执行检查
[实验与实现](../../lab/README.md)，相关检查：`test_affine_time_derivative`, `test_rk4_affine_endpoint`, `flow_matching.json`。测试只覆盖列出的数值行为，不表示本技能已通过真实agent项目验收。

## 反例与禁止推断
当必要输入缺失，先输出缺口和分支，不填补虚构参数；本包数值通过不构成用户真实生物学结论的证据。
