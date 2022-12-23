
# 导入需要测试的操作op和任务job
from complex_job import *

# 写一个简单用例
def test_get_total_size():
    file_sizes = {"file1": 400, "file2": 50}
    result = get_total_size(file_sizes)
    assert result == 450

# 测试
def test_diamond():
    # 执行job
    res = diamond.execute_in_process()
    
    # 看看是否成功，并且输出结果
    assert res.success
    assert res.output_for_node("get_total_size") > 0
