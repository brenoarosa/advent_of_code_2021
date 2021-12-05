from typing import List


def count_increased_measures(lines: List[int]) -> int:
    count = 0
    previous, lines = lines[0], lines[1:]

    for line in lines:
        if line > previous:
            count += 1
        previous = line
    return count

def window_measurements(lines: List[int]) -> List[int]:
    windowed_measurements = [None] * (len(lines)-2)

    for i in range(2, len(lines)):
        windowed_measurements[i-2] = lines[i-2] + lines[i-1] + lines[i]

    return windowed_measurements


if __name__ == '__main__':
    with open("inputs/input_01.txt") as fin:
        lines = fin.readlines()
    # cast to int
    lines = [int(line.rstrip()) for line in lines]

    print(count_increased_measures(lines))
    print(count_increased_measures(window_measurements(lines)))
