import pytest

from daily_byte.valid_palindrome.solution import valid_palindrome


@pytest.mark.parametrize(
    'test_input,expected', [
        ('level', True),
        ('algorithm', False),
        ('A man, a plan, a canal: Panama.', True)
    ]
)
def test_valid_palindrome(test_input, expected):
    assert valid_palindrome(test_input) == expected
