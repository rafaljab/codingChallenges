import pytest

from leetcode.roman_to_integer.solution import roman_to_int


@pytest.mark.parametrize(
    's, expected', [
        ('III', 3),
        ('LVIII', 58),
        ('MCMXCIV', 1994)
    ]
)
def test_roman_to_int(s, expected):
    assert roman_to_int(s) == expected
