import pytest

from daily_byte.jewels_and_stones.solution import jewels_and_stones


@pytest.mark.parametrize(
    'jewels, stones, expected', [
        ('abc', 'ac', 2),
        ('Af', 'AaaddfFf', 3),
        ('AYOPD', 'ayopd', 0)
    ]
)
def test_jewels_and_stones(jewels, stones, expected):
    assert jewels_and_stones(jewels, stones) == expected
