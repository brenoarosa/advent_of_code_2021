import pytest
from advent.puzzle_06 import parse_input, calculate_state

example_input = "3,4,3,1,2"


def test_parse_input():
    input = parse_input(example_input)
    assert input == [3,4,3,1,2]

def test_calculate_state_18():
    initial_state = parse_input(example_input)
    assert calculate_state(initial_state, 18) == 26

def test_calculate_state_80():
    initial_state = parse_input(example_input)
    assert calculate_state(initial_state, 80) == 5934

def test_calculate_state_256():
    initial_state = parse_input(example_input)
    assert calculate_state(initial_state, 256) == 26984457539
