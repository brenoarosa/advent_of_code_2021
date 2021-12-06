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

@pytest.mark.parametrize("filter_diagonal, expected", [
    (True, 5),
    (False, 12),
])
def test_calculate_vent_map(filter_diagonal, expected):
    vents = parse_input(example_input)
    assert calculate_vent_map(vents, filter_diagonal) == expected
