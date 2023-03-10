import pytest

from daily_byte.valid_anagram.solution import valid_anagram


@pytest.mark.parametrize(
    's, t, expected', [
        ('cat', 'tac', True),
        ('listen', 'silent', True),
        ('program', 'function', False)
    ]
)
def test_valid_anagram(s, t, expected):
    assert valid_anagram(s, t) == expected
