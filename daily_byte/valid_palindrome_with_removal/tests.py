import pytest

from daily_byte.valid_palindrome_with_removal.solution import valid_palindrome_with_removal


@pytest.mark.parametrize(
    'test_input, expected', [
        ('abcba', True),
        ('foobof', True),
        ('abccab', False)
    ]
)
def test_valid_palindrome_with_removal(test_input, expected):
    assert valid_palindrome_with_removal(test_input) == expected
