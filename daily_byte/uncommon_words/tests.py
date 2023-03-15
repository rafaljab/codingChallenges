import pytest

from daily_byte.uncommon_words.solution import uncommon_words


@pytest.mark.parametrize(
    'sentence1, sentence2, expected', [
        ('the quick', 'brown fox', ['the', 'quick', 'brown', 'fox']),
        ('the tortoise beat the haire', 'the tortoise lost to the haire', ['beat', 'to', 'lost']),
        ('copper coffee pot', 'hot coffee pot', ['copper', 'hot']),
        ('on the one hand and on the other hand', 'the one thing', ['on', 'hand', 'and', 'other', 'thing'])
    ]
)
def test_uncommon_words(sentence1, sentence2, expected):
    assert uncommon_words(sentence1, sentence2).sort() == expected.sort()
