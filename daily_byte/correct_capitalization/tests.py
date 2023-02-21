import pytest

from daily_byte.correct_capitalization.solution import correct_capitalization


@pytest.mark.parametrize(
    'test_input,expected', [
        ('USA', True),
        ('Calvin', True),
        ('compUter', False),
        ('coding', True)
    ]
)
def test_correct_capitalization(test_input, expected):
    assert correct_capitalization(test_input) == expected
