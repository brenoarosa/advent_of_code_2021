from typing import List, Tuple


def get_total_bits_set(reports: List[int], report_len: int) -> List[int]:
    def is_bit_set(x: int, bit_position: int) -> bool:
        return (x & (1 << bit_position) != 0)

    total_bits_set = [0] * report_len
    for report in reports:
        for i in range(report_len):
            bit_position = report_len - i - 1
            total_bits_set[bit_position] += is_bit_set(report, bit_position)

    return total_bits_set

def extract_gamma_epsilon(reports: List[int], report_len: int = 12) -> Tuple[int, int]:
    gamma = 0
    epsilon = 0

    total_bits_set = get_total_bits_set(reports, report_len)

    for i in range(report_len):
        bit_position = report_len - i - 1

        gamma += int(total_bits_set[bit_position] >= (len(reports) / 2)) << bit_position
        epsilon += int(total_bits_set[bit_position] < (len(reports) / 2)) << bit_position

    return gamma, epsilon


def share_bit(x: int, y: int, bit_position: int) -> bool:
    return (~(x ^ y) & (1 << bit_position) != 0)

def extract_most_matching(reports: List[int], ref_val: int, report_len: int) -> int:
    bit_position = report_len - 1

    to_str = lambda x: ["{0:05b}".format(i) for i in x]
    while len(reports) > 1:
        print(to_str(reports))
        reports = [
            report for report in reports
            if share_bit(ref_val, report, bit_position)
        ]
        bit_position -= 1

    print(to_str(reports))
    return reports[0]

def extract_o2_co2(reports: List[int], report_len: int = 12) -> Tuple[int, int]:

    total_bits_set = get_total_bits_set(reports, report_len)

    most_common_bits_list = [int(v >= (len(reports)/2)) for v in total_bits_set]
    most_common_bits = sum([v << i for i, v in enumerate(most_common_bits_list)])

    least_common_bits_list = [int(v <= (len(reports)/2)) for v in total_bits_set]
    least_common_bits = sum([v << i for i, v in enumerate(least_common_bits_list)])

    o2 = extract_most_matching(reports, most_common_bits, report_len)
    co2 = extract_most_matching(reports, least_common_bits, report_len)
    print("most_common")
    print("{:012b}".format(most_common_bits))
    print("{:012b}".format(o2))
    print("least_common")
    print("{:012b}".format(least_common_bits))
    print("{:012b}".format(co2))
    return o2, co2


if __name__ == '__main__':
    with open("inputs/input_03.txt") as fin:
        lines = fin.readlines()
    reports = [int(line.rstrip(), 2) for line in lines]

    gamma, epsilon = extract_gamma_epsilon(reports)
    print(gamma * epsilon)
    o2, co2 = extract_o2_co2(reports)
    print(o2 * co2)
