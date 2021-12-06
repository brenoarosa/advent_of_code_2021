from dataclasses import dataclass
from typing import List, Tuple
import numpy as np

@dataclass
class Vent:
    x1: int
    y1: int

    x2: int
    y2: int


def parse_input(input_str: str) -> List[Vent]:
    lines = input_str.strip().split("\n")

    to_xy = lambda coord: (int(coord.split(",")[0]), int(coord.split(",")[1]))
    vents = []
    for line in lines:
        coord1, coord2 = line.strip().split(" -> ")
        x1, y1 = to_xy(coord1)
        x2, y2 = to_xy(coord2)
        vents.append(Vent(x1, y1, x2, y2))

    return vents

def get_map_size(vents: List[Vent]) -> Tuple[int, int]:
    Y = max([max(v.y1, v.y2) for v in vents]) + 1
    X = max([max(v.x1, v.x2) for v in vents]) + 1
    return Y, X

def calculate_vent_map(vents: List[Vent], filter_diagonal: bool = True) -> int:
    if filter_diagonal:
        vents = [v for v in vents if ((v.x1 == v.x2) or (v.y1 == v.y2))]

    map_size = get_map_size(vents)
    mask = np.zeros(map_size, dtype=int)
    game_map = np.zeros(map_size, dtype=int)

    for vent in vents:
        y_order = 2 * int(vent.y2 >= vent.y1) - 1
        x_order = 2 * int(vent.x2 >= vent.x1) - 1

        y_range = list(range(vent.y1, (vent.y2 + y_order), y_order))
        x_range = list(range(vent.x1, (vent.x2 + x_order), x_order))
        mask[y_range, x_range] = 1

        game_map += mask
        mask[:, :] = 0

    points = game_map[game_map >= 2].astype(bool).sum()
    return points


if __name__ == '__main__':
    with open("inputs/input_05.txt") as fin:
        input_str = fin.read().rstrip()

    vents = parse_input(input_str)
    print(calculate_vent_map(vents))
    print(calculate_vent_map(vents, False))
