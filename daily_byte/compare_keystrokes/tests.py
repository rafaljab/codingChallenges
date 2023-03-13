import pytest

from daily_byte.compare_keystrokes.solution import compare_keystrokes


@pytest.mark.parametrize(
    's, t, expected', [
        ('#ABC#', 'CD##AB', True),
        ('ABC#', 'CD##AB', True),
        ('como#pur#ter', 'computer', True),
        ('cof#dim#ng', 'code', False)
    ]
)
def test_compare_keystrokes(s, t, expected):
    assert compare_keystrokes(s, t) == expected
