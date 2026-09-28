# 可执行数值实验：范围与运行方式

这些代码是独立教育性实现，不是20篇原论文软件，也不是生产级临床统计或大规模OT库。

## 已执行
六个模拟见`../results/execution_report.json`；原始日志与实际版本在`../results/`。数值测试对解析性质、SciPy优化器及statsmodels结果交叉校验。全部在CPU执行。

```bash
# 从压缩包解压后的omics_skill_research目录运行；先使用独立环境配置依赖。
python -m lab.run_all
python -m pytest -q tests --junitxml=results/pytest.xml
```

上面第一条会覆盖本地results下同名实验输出；需要保留本版记录时先复制results。

## 模块和问题
|模块|内容|不能据此宣称|
|---|---|---|
|statistics.py|BH/BY、raw count聚合、独立单位/选择性检验反例|已运行真实NB differential expression|
|causal.py|独立样本下crossfit AIPW、混杂/collider反例|观察数据已识别因果、自动处理空间干扰|
|spatial.py|坐标扰动、重建邻域、表达混合与niche漂移|真实污染率估计、分子守恒、校准置信区间|
|transport.py|稠密log-Sinkhorn/UOT、SciPy独立oracle|POT已运行、GW已实现、支持百万细胞|
|flow.py|线性路径、PyTorch CFM、RK4与解析耦合|CellFlow已复现、真实恶变路径/增长死亡已识别|

## 数值限制
OT实现要求有限成本、严格正质量，显式拒绝零支持和非法值；零质量需先裁剪并保留索引映射。没有稀疏禁止边、GW、partial OT或分布式计算。UOT样本配对归一化会改变所代表的总体边际，须报告。

AIPW中的标准误是独立行假设下的演示；真实donor-cluster数据须另建cluster crossfit/variance协议。空间混合只模拟期望表达而非分子级计数转移。

`requirements-tested.txt`记录**本环境已安装的版本**，并非跨平台lockfile，也未在全新Windows/conda环境进行安装验证。官方POT/FM/moscot/NicheCompass没有执行。六个notebook调用这些本地模块，不重复粘贴第三方实现。
