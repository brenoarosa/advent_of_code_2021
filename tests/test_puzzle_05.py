import pytest
from advent.puzzle_05 import Vent, parse_input, calculate_vent_map

example_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

def test_parse_input_draws():
    vents = parse_input(example_input)
    expected = [
        Vent(0, 9, 5, 9),
        Vent(8, 0, 0, 8),
        Vent(9, 4, 3, 4),
        Vent(2, 2, 2, 1),
        Vent(7, 0, 7, 4),
        Vent(6, 4, 2, 0),
        Vent(0, 9, 2, 9),
        Vent(3, 4, 1, 4),
        Vent(0, 0, 8, 8),
        Vent(5, 5, 8, 2),
    ]
    assert vents == expected

def test_calculate_vent_map():
    vents = parse_input(example_input)
    assert calculate_vent_map(vents) == 5

"""
@pytest.mark.parametrize("test_input, expected", [
    ((0b10, 0b10, 0), True),
    ((0b10, 0b10, 1), True),
    ((0b10, 0b10, 2), True),
    ((0b10, 0b11, 0), False),
    ((0b10, 0b11, 1), True),
    ((0b10, 0b11, 3), True),
    ((0b10001, 0b111, 2), False),
])
def test_share_bit(test_input, expected):
    assert share_bit(*test_input) == expected
"""

