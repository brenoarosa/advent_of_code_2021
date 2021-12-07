from typing import List

LIFE_CICLE = 7
INCUBATION_TIME = 8

def parse_input(input_str: str) -> List[int]:
    line = input_str.strip()
    return [int(i) for i in line.split(",")]

def calculate_state(state: List[int], days: int) -> List[int]:

    for day in range(days):
        print(f"Calculating day={day}")
        next_state = []
        new_fishes = 0
        for fish_time in state:
            if fish_time == 0:
                new_fishes += 1

            if fish_time <= LIFE_CICLE:
                next_fish_time = (fish_time - 1) % LIFE_CICLE
            else:
                next_fish_time = (fish_time - 1)

            next_state.append(next_fish_time)

        for _ in range(new_fishes):
            next_state.append(INCUBATION_TIME)

        state = next_state

    return state


if __name__ == '__main__':
    with open("inputs/input_06.txt") as fin:
        input_str = fin.read().rstrip()

    initial_state = parse_input(input_str)
    print(len(calculate_state(initial_state, 80)))
    print(len(calculate_state(initial_state, 256)))
