import pytest

from questions.reverse_string.solution import reverse_string


@pytest.mark.parametrize(
    "test_input, expected", [
        ('Cat', 'taC'),
        ('The Daily Byte', 'etyB yliaD ehT'),
        ('civic', 'civic')
    ]
)
def test_reverse_string(test_input, expected):
    assert reverse_string(test_input) == expected
