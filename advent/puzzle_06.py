from typing import List

LIFE_CICLE = 7
INCUBATION_TIME = 9

def parse_input(input_str: str) -> List[int]:
    line = input_str.strip()
    return [int(i) for i in line.split(",")]

def calculate_state(state: List[int], days: int) -> int:

    fish_timer_counter = [0] * INCUBATION_TIME
    for fish_time in state:
        fish_timer_counter[fish_time] += 1

    for day in range(days):
        next_fish_timer_counter = [0] * INCUBATION_TIME

        next_fish_timer_counter[INCUBATION_TIME-1] += fish_timer_counter[0]
        next_fish_timer_counter[LIFE_CICLE-1] += fish_timer_counter[0]

        for i in range(INCUBATION_TIME-1):
            next_fish_timer_counter[i] += fish_timer_counter[i+1]

        fish_timer_counter = next_fish_timer_counter

    return sum(fish_timer_counter)


if __name__ == '__main__':
    with open("inputs/input_06.txt") as fin:
        input_str = fin.read().rstrip()

    initial_state = parse_input(input_str)
    print(calculate_state(initial_state, 80))
    print(calculate_state(initial_state, 256))
