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

def get_board_winning_round_and_score(numbers_draw: List[int], board: np.ndarray) -> Tuple[int, int]:
    board_mask = np.zeros((5, 5))

    for game_round, draw in enumerate(numbers_draw):
        board_mask += np.equal(board, draw)

        if (5 in board_mask.sum(axis=0)) or (5 in board_mask.sum(axis=1)):
            sum_numbers = int(((1-board_mask) * board).sum())
            board_score = draw * sum_numbers
            return game_round, board_score

def calculate_board_results(numbers_draw: List[int], boards: List[np.ndarray]) -> Tuple[List[int], List[int]]:

    winning_round = [None] * len(boards)
    winning_score = [None] * len(boards)
    for i, board in enumerate(boards):
        game_round, score = get_board_winning_round_and_score(numbers_draw, board)
        winning_round[i] = game_round
        winning_score[i] = score

    return winning_round, winning_score

def get_first_winner_score(numbers_draw: List[int], boards: List[np.ndarray]) -> int:
    winning_round, winning_score = calculate_board_results(numbers_draw, boards)
    winner_board = np.argmin(winning_round)
    return winning_score[winner_board]

def get_last_winner_score(numbers_draw: List[int], boards: List[np.ndarray]) -> int:
    winning_round, winning_score = calculate_board_results(numbers_draw, boards)
    winner_board = np.argmax(winning_round)
    return winning_score[winner_board]

if __name__ == '__main__':
    with open("inputs/input_04.txt") as fin:
        input_str = fin.read().rstrip()

    numbers_draw, boards = parse_input(input_str)
    print(get_first_winner_score(numbers_draw, boards))
    print(get_last_winner_score(numbers_draw, boards))
