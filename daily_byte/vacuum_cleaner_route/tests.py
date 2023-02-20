import pytest

from daily_byte.vacuum_cleaner_route.solution import vacuum_cleaner_route


@pytest.mark.parametrize(
    'test_input,expected', [
        ('LR', True),
        ('URURD', False),
        ('RUULLDRD', True)
    ]
)
def test_vacuum_cleaner_route(test_input, expected):
    assert vacuum_cleaner_route(test_input) == expected
