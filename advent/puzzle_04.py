from io import StringIO
from typing import List, Tuple
import numpy as np

def parse_input(input_str: str) -> Tuple[List[int], List[np.ndarray]]:
    lines = input_str.strip().split("\n")

    draws = [int(x) for x in lines[0].strip().split(",")]
    boards = []

    i = 2
    while i < len(lines) - 4:
        board_str = StringIO("\n".join(lines[i:i+5]))
        board = np.loadtxt(board_str, dtype=int)
        boards.append(board)

        i += 5 + 1

    return draws, boards

def get_winner_score(numbers_draw: List[int], boards: List[np.ndarray]) -> int:

    boards_masks = []
    for i in range(len(boards)):
        board_mask = np.zeros((5, 5))
        boards_masks.append(board_mask)

    for draw in numbers_draw:
        for i, board in enumerate(boards):
            board_mask = boards_masks[i]
            board_mask += np.equal(board, draw)
            boards_masks[i] = board_mask

            if (5 in board_mask.sum(axis=0)) or (5 in board_mask.sum(axis=1)):
                sum_numbers = int(((1-board_mask) * board).sum())
                return draw * sum_numbers

    return 0



if __name__ == '__main__':
    with open("inputs/input_04.txt") as fin:
        input_str = fin.read().rstrip()

    numbers_draw, boards = parse_input(input_str)
    print(get_winner_score(numbers_draw, boards))
