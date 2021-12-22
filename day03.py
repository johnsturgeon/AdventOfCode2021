from typing import List


def most_common_in_column(position: int, diagnostic_report: List) -> str:
    count = len(diagnostic_report)
    total = 0
    for line in diagnostic_report:
        total += int(line[position])
    if total >= count / 2:
        return '1'
    return '0'


def gamma_from_list(diagnostic_report: List) -> str:
    line_length = len(diagnostic_report[0])
    gamma_string = ''
    for i in range(line_length):
        gamma_string += most_common_in_column(i, diagnostic_report)
    return gamma_string


def epsilon_from_gamma(gamma_string) -> str:
    epsilon_string = ''
    for x in range(len(gamma_string)):
        if gamma_string[x] == '1':
            epsilon_string += '0'
        else:
            epsilon_string += '1'
    return epsilon_string


def sub_report_from_column(invert: bool, position: int, diagnostic_report: List[str]) -> List[str]:
    most_common = most_common_in_column(position, diagnostic_report)
    if invert:
        if most_common == '1':
            most_common = '0'
        else:
            most_common = '1'
    most_common_list = []
    for line in diagnostic_report:
        if line[position] == most_common:
            most_common_list.append(line)
    return most_common_list


def get_diagnostic_rating(invert: bool, diagnostic_report: List) -> int:
    line_length = len(diagnostic_report[0])
    updated_report = diagnostic_report
    for x in range(line_length):
        updated_report = sub_report_from_column(invert, x, updated_report)
        if len(updated_report) == 1:
            break
    return int(updated_report[0], 2)


def get_life_support_rating(diagnostic_report: List) -> int:
    o2_rating = get_diagnostic_rating(False, diagnostic_report)
    c02_rating = get_diagnostic_rating(True, diagnostic_report)
    return o2_rating * c02_rating


def power_consumption(diagnostic_report: List) -> int:
    gamma_string = gamma_from_list(diagnostic_report)
    epsilon_string = epsilon_from_gamma(gamma_string)
    return int(gamma_string, 2) * int(epsilon_string, 2)

