import pytest

from daily_byte.spot_the_difference.solution import spot_the_difference


@pytest.mark.parametrize(
    's, t, expected', [
        ('foobar', 'barfoot', 't'),
        ('ide', 'idea', 'a'),
        ('coding', 'ingcod', '')
    ]
)
def test_spot_the_difference(s, t, expected):
    assert spot_the_difference(s, t) == expected
