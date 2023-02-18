import pytest

from leetcode.two_sum.solution import two_sum


@pytest.mark.parametrize(
    'input_nums,input_target,expected', [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
)
def test_two_sum(input_nums, input_target, expected):
    assert two_sum(nums=input_nums, target=input_target) == expected
