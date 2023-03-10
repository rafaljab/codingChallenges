import pytest

from daily_byte.validate_characters.solution import validate_characters


@pytest.mark.parametrize(
    'test_input, expected', [
        ('(){}[]', True),
        ('(({[]}))', True),
        ('{(})', False)
    ]
)
def test_validate_characters(test_input, expected):
    assert validate_characters(test_input) == expected
