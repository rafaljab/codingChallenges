import pytest

from daily_byte.intersection_of_numbers.solution import intersection_of_numbers, intersection_of_numbers_2


@pytest.mark.parametrize(
    'nums1, nums2, expected', [
        ([2, 4, 4, 2], [2, 4], [2, 4]),
        ([1, 2, 3, 3], [3, 3], [3]),
        ([2, 4, 6, 8], [1, 3, 5, 7], [])
    ]
)
def test_intersection_of_numbers(nums1, nums2, expected):
    assert intersection_of_numbers(nums1, nums2) == expected


@pytest.mark.parametrize(
    'nums1, nums2, expected', [
        ([2, 4, 4, 2], [2, 4], [2, 4]),
        ([1, 2, 3, 3], [3, 3], [3]),
        ([2, 4, 6, 8], [1, 3, 5, 7], [])
    ]
)
def test_intersection_of_numbers_2(nums1, nums2, expected):
    assert intersection_of_numbers_2(nums1, nums2) == expected
