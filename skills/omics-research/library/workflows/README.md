# 项目工作流配置

本目录将知识章转成可填写契约；`null`是故意保留的项目输入，不应自动替换成猜测。

- `statistical_design.yaml`、`testing_family.yaml`：独立重复、设计矩阵、selection与检验家族。
- `causal_contract.yaml`：先定义识别问题，再选估计器；模型调整不能替代DAG。
- `spatial_error.yaml`：明确真实误差模型和人为压力测试的区别。
- `ot_contract.yaml`、`fm_contract.yaml`：把成本、质量、耦合、路径与ODE拆开。
- `uncertainty_contract.yaml`：采样、测量、算法、结构不确定性分开报告。
- `reproduction_manifest.yaml`：记录原论文目标图、输入哈希和精确版本。

## 原论文执行器

人工审阅上游代码，预先取得输入，填写manifest并把status设为`ready_for_local_execution`后：

```bash
python -m workflows.run_reproduction workflows/my_filled_manifest.yaml --output /path/to/new_run_log
```

执行器不安装、不联网、不使用shell命令字符串；会执行你提供的本地argv，因此仍须审阅其权限和代码。成功退出只代表命令执行与输出存在，**scientific_acceptance始终由独立的项目验收判断**。

## edgeR模板
`pseudobulk_edger.R`使用raw-count pseudobulk，支持独立患者两组或完整donor配对。其他重复样本、batch协变量、多组、多population联合检验需扩展并审核设计。它在本轮**未执行，R语法也未由R解释器验证**；不把Python测试通过算作R结果。

来源：[edgeR官方入口G34](../references/GAP_SOURCES.md#g34)；统计条件详见[统计章](../knowledge/02_statistics.md)。
