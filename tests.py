import pytest

from letters import num_buracos


@pytest.mark.parametrize(
    'word, expected', [
        ('banana', 4),
        ('Banana', 5),
        ('olho', 2),
        ('çzt', 0),
    ]
)
def test_hole_counter(word, expected):
    assert(num_buracos(word) == expected)


@pytest.mark.parametrize(
    'word, expected', [
        ('batata', 0),
        ('Batata', 0),
        ('python', 3),
        ('çzt', 1),
    ]
)
def test_fail_hole_counter(word, expected):
    assert(num_buracos(word) != expected)
