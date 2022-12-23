
# 测试单个逻辑
def nabisco_cereals(cereals):
    """Cereals manufactured by Nabisco"""
    return [row for row in cereals if row["mfr"] == "N"]

# 假设传入 cereals ，assert 是否能得到预期的数据
def test_nabisco_cereals():
    cereals = [
        {"name": "cereal1", "mfr": "N"},
        {"name": "cereal2", "mfr": "K"},
    ]
    result = nabisco_cereals(cereals)
    
    assert len(result) == 1
    assert result == [{"name": "cereal1", "mfr": "N"}]
    
    