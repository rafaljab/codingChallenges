import pytest

from daily_byte.remove_adjacent_duplicates.solution import remove_adjacent_duplicates


@pytest.mark.parametrize(
    's, expected', [
        ('abccba', ''),
        ('foobar', 'fbar'),
        ('abccbefggfe', 'a')
    ]
)
def test_remove_adjacent_duplicates(s, expected):
    assert remove_adjacent_duplicates(s) == expected
