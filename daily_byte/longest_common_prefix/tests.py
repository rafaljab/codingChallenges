import pytest

from daily_byte.longest_common_prefix.solution import longest_common_prefix


@pytest.mark.parametrize(
    'data, expected', [
        (['colorado', 'color', 'cold'], 'col'),
        (['a', 'b', 'c'], ''),
        (['spot', 'spotty', 'spotted'], 'spot')
    ]
)
def test_longest_common_prefix(data, expected):
    assert longest_common_prefix(data) == expected
