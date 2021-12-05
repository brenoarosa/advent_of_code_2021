import pytest
from advent.puzzle_04 import parse_input, get_winner_score

example_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


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

def test_parse_input_draws():
    draws, boards = parse_input(example_input)
    assert draws == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def test_get_winner_score():
    numbers_draw, boards = parse_input(example_input)
    assert get_winner_score(numbers_draw, boards) == 4512
