"""可修改的小测试示例：另选输入，保留自己的预期与解释。

测试通过参数接收课程 fixture，--impl 才能切换候选实现。
不要直接 from operations import pop_last 绕过这个开关。
"""

import numpy as np


def test_my_pop_example(pop_last):
    items = [7, 4]

    result = pop_last(items)

    assert result == 4
    assert items == [7]


def test_my_pop_last_removes_last_item(pop_last):
    items = [10, 20, 30]

    result = pop_last(items)

    assert result == 30
    assert items == [10, 20]


def test_my_pop_last_empty_list_returns_none(pop_last):
    items = []

    result = pop_last(items)

    assert result is None
    assert items == []


def test_my_positive_squares_filters_and_keeps_duplicates(positive_squares):
    values = [-2, 0, 3, 1, 3]

    result = positive_squares(values)

    assert result == [9, 1, 9]
    assert result is not values
    assert values == [-2, 0, 3, 1, 3]


def test_my_positive_squares_accepts_numpy_array(positive_squares):
    values = np.array([-2, 0, 3, 1, 3], dtype=int)
    before = values.copy()

    result = positive_squares(values)

    assert result == [9, 1, 9]
    assert isinstance(result, list)
    np.testing.assert_array_equal(values, before)


def test_my_positive_square_map_returns_new_dict(positive_square_map):
    record = {"a": -2, "b": 3, "c": 0, "d": 3}
    before = record.copy()

    result = positive_square_map(record)

    assert result == {"b": 9, "d": 9}
    assert list(result) == ["b", "d"]
    assert result is not record
    assert record == before
    assert list(record) == list(before)
