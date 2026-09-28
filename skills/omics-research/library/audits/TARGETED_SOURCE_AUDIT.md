# 定向补充材料与源码审计

## 为什么没有统一的“读完/复现”标签
分别记录：取得材料、定向阅读、全量阅读、源码核查、官方运行、原图复现。源文件看过不等于软件运行；独立实现通过测试不等于原论文复现。

## NicheCompass [G19–G20]
核查44页Supplementary Information中物理页41–43的方法/训练/评价定义；另查看物理页36相关程序重叠图。主要提取posterior comparison语义、模拟真值的使用、置换零假设及综合分数定义。训练设置记录包括Adam学习率1e−3、调度patience=4/factor=0.1、early stopping=8；**这些是该SI中的特定协议，不作为新课题通用参数。**

代码入口区分software归档`10.5281/zenodo.14621258`与paper-analysis归档`10.5281/zenodo.14632687`。没有下载运行这两个归档；没有逐行审读原软件实现。完整44页的所有图、其他附件和peer-review没有全部核读。

## stClinic [G21]
核查主文对training-time dynamic graph的定义、连续关系局限与code availability。文章记录版本0.0.10，原论文代码归档为`10.5281/zenodo.15246396`。SI链接未成功打开，不填充未知超参或复现结果。

## POT [G17–G18]
核查官方API及`ot.unbalanced._sinkhorn`渲染源码的默认正则约定、kernel与更新。文档记录从0.9.5起默认`reg_type='kl'`；与旧entropy约定相比，参考测度改变会影响UOT最优计划和质量，不仅是显示格式。查看`sinkhorn_unbalanced2`时必须明确linear或total返回值。

`lab/transport.py`是本包独立实现，以解析例和SciPy优化器作交叉检查。**没有安装或运行POT。**当前web源码没有固定commit，不可用访问日期替代commit hash。

## Meta flow_matching [G25]
核查`path/affine.py`的`AffineProbPath.sample`和`CondOTProbPath`。后者构造线性调度，不求解端点OT。方法名中的OT不是已执行OT的证据。只阅读当前main分支，未固定commit、未运行官方包；未复制有许可约束的第三方文件。

## 下一步原图复现的准入
每个figure选择确切panel、原始输入、参数、软件归档及定量验收方式。运行[复现清单](../workflows/reproduction_manifest.yaml)，留下执行日志、退出码与文件哈希。当前包的完整状态见[逐篇矩阵](PAPER_REPRODUCTION_MATRIX.md)。

来源链接及阅读范围：[GAP_SOURCES.md](../references/GAP_SOURCES.md)。机器记录：[source_audit.json](source_audit.json)。
