import pytest

from daily_byte.add_binary.solution import add_binary


@pytest.mark.parametrize(
    'a, b, expected', [
        ('100', '1', '101'),
        ('11', '1', '100'),
        ('1', '0', '1'),
        ('11', '11', '110')
    ]
)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected
