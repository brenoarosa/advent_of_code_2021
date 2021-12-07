import pytest
from advent.puzzle_06 import parse_input, calculate_state

example_input = "3,4,3,1,2"


def test_parse_input():
    input = parse_input(example_input)
    assert input == [3,4,3,1,2]

def test_calculate_state_18():
    expected = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
    initial_state = parse_input(example_input)
    assert calculate_state(initial_state, 18) == expected

def test_calculate_state_80():
    initial_state = parse_input(example_input)
    assert len(calculate_state(initial_state, 80)) == 5934

def test_calculate_state_256():
    initial_state = parse_input(example_input)
    assert len(calculate_state(initial_state, 256)) == 26984457539
