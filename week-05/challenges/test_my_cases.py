"""A 题个人用例：保留首次顺序，统计重复情况。

测试通过同名 fixture 接收实现，--challenge-impl 才能切换候选。
不要直接导入 challenges.work 或参考实现绕过这个开关。
"""


def test_my_summarize_first_case(summarize_values):
    values = [3, 1, 3, 2, 1, 3]
    before = values.copy()

    result = summarize_values(values)

    assert result["unique"] == [3, 1, 2]
    assert result["counts"] == {3: 3, 1: 2, 2: 1}
    assert result["repeated"] == {1, 3}
    assert values == before


def test_my_summarize_second_case(summarize_values):
    values = [4, 4, -1, 0, -1, 4]
    before = values.copy()

    result = summarize_values(values)

    assert result["unique"] == [4, -1, 0]
    assert result["counts"] == {4: 3, -1: 2, 0: 1}
    assert result["repeated"] == {4, -1}
    assert values == before


def test_my_summarize_empty_case(summarize_values):
    values = []
    before = values.copy()

    result = summarize_values(values)

    assert set(result) == {"unique", "counts", "repeated"}
    assert result == {"unique": [], "counts": {}, "repeated": set()}
    assert values == before
