# 从五项知识缺口到实际课题的学习路线

## 第一阶段：先消除会使整篇结论失效的错误
读[统计章](knowledge/02_statistics.md)，运行notebook01–02；填统计设计与检验家族配置。再读[因果章](knowledge/03_causal.md)，运行notebook03。验收不是记住公式，而是能解释：为什么一万个细胞不等于一万个donor、为什么BH修不好无效p值、为什么调整所有变量可能出错。

## 第二阶段：确认观察对象没有被上游处理改变
读[测量误差章](knowledge/04_spatial_error.md)，运行notebook04。画出原始分子/图像到细胞表达、到邻域、到embedding、到结论的实际数据流。在最上游合理位置加入误差，重新构建后续对象；不要只扰动最终latent后称已覆盖测量误差。

## 第三阶段：再连接OT与flow matching
依次读[OT章](knowledge/05_ot.md)和[FM章](knowledge/06_flow_matching.md)，运行notebook05–06。先写完整成本/质量/正则问题，再选求解器；先确定训练边际和端点配对，再定义条件路径。验证解析场、数值积分和留出端点，不把漂亮箭头当真实历史。

## 第四阶段：形成可复现的证据包
读[复现章](knowledge/01_reproduction.md)和[不确定性章](knowledge/07_uncertainty.md)。核查SI与源码，填写原图manifest，按真实患者层级传播不确定性。每个结果标记原文事实F、综合规则S、待验证P或本轮执行E。

## 针对项目的入口
DyMoTree解释性：08→21→22→28，区分重建、program语义、命运预测与driver稳定性，避免把posterior比较自动当频率学显著性。

NicheFlux：04→24→07→25→26→23。先确认niche表示与整合保持目标生物学，再解释coupling和flow；UOT归一化后的实际边际须与ODE初始分布一致，普通FM不自动处理生灭。

本路线不预先保证复杂模型胜出，也不设置所有数据通用的FDR以外的性能合格线。正式项目阈值须在测试前依据科学目标、模拟和样本规模说明。
