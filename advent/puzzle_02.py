from typing import List, Tuple


def get_final_position(instructions: List[Tuple[str, int]]) -> Tuple[int, int]:
    x = 0
    y = 0

    for cmd, value in instructions:
        if cmd == "forward":
            x += value
        elif cmd == "up":
            y -= value
        elif cmd == "down":
            y += value
        else:
            raise Exception("Unexpect value")

    return x, y

def get_corrected_final_position(instructions: List[Tuple[str, int]]) -> Tuple[int, int]:
    x = 0
    y = 0
    aim = 0

    for cmd, value in instructions:
        if cmd == "forward":
            x += value
            y += aim * value
        elif cmd == "up":
            aim -= value
        elif cmd == "down":
            aim += value
        else:
            raise Exception("Unexpect value")

    return x, y



if __name__ == '__main__':
    with open("inputs/input_02.txt") as fin:
        lines = fin.readlines()
    instructions = [line.rstrip().split(" ") for line in lines]
    instructions = [(instruction[0], int(instruction[1])) for instruction in instructions]

    x, y = get_final_position(instructions)
    print(x * y)
    x, y = get_corrected_final_position(instructions)
    print(x * y)
