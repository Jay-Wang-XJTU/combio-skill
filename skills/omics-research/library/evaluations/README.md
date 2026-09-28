# 验证对象必须分开

- **数值测试**：`tests/test_numerics.py`及其他测试文件，执行结果在`results/pytest.xml`。检验的是本地函数/结构。
- **六个合成实验**：`results/execution_report.json`，展示已知真值下的反例或数值性质。
- **Notebook**：`notebooks/`，保存实际执行输出；不是原论文图复现。
- **Agent行为案例**：`cases.json`共38个（原22+新增16），全部`not_run`。没有调用另一agent完成这些案例，不能宣称behavior-tested。

行为评测需保存完整输入、agent/model版本、工具调用、实际回答、每条rubric判断及人工复核。没有观察回答不能凭关键词lint判通过。结构测试不能替代科学正确性评价。
