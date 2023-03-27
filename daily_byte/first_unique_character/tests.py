import pytest

from daily_byte.first_unique_character.solution import first_unique_character, first_unique_character_2


@pytest.mark.parametrize(
    'text, expected', [
        ('abcabd', 2),
        ('thedailybyte', 1),
        ('developer', 0),
        ('abcabc', -1)
    ]
)
def test_first_unique_character(text, expected):
    assert first_unique_character(text) == expected


@pytest.mark.parametrize(
    'text, expected', [
        ('abcabd', 2),
        ('thedailybyte', 1),
        ('developer', 0),
        ('abcabc', -1)
    ]
)
def test_first_unique_character_2(text, expected):
    assert first_unique_character_2(text) == expected

