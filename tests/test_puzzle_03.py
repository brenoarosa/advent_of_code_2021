import pytest
from advent.puzzle_03 import (share_bit, extract_o2_co2, get_total_bits_set)

example_reports = [
    0b00100,
    0b11110,
    0b10110,
    0b10111,
    0b10101,
    0b01111,
    0b00111,
    0b11100,
    0b10000,
    0b11001,
    0b00010,
    0b01010
]


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

def test_get_total_bits_set():
    total_bits_set = get_total_bits_set(example_reports, 5)
    assert total_bits_set == [5, 7, 8, 5, 7]

def test_extract_o2_co2():
    o2, co2 = extract_o2_co2(example_reports, 5)
    assert o2 == 0b10111
    assert co2 == 0b01010
