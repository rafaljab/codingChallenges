import pytest

from daily_byte.string_permutations.solution import string_permutations


@pytest.mark.parametrize(
    's, expected', [
        ('c7w2', ['c7w2', 'c7W2', 'C7w2', 'C7W2']),
        ('34Fbc', ['34fbc', '34FBc', '34Fbc', '34fBc', '34fbC', '34FBC', '34FbC', '34fBC'])
    ]
)
def test_string_permutations(s, expected):
    assert string_permutations(s).sort() == expected.sort()
