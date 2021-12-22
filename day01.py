from typing import List


def number_increases(depth_measurements: List) -> int:
    prev_depth = depth_measurements[0]
    first_run = True
    count = 0
    for measurement in depth_measurements:
        if first_run:
            first_run = False
            continue
        if measurement > prev_depth:
            count += 1
        prev_depth = measurement

    return count


def sum_three_safely(start: int, in_list: List) -> int:
    """ Safely sums three items from a list, returning zero if it would overflow """
    if start + 2 >= len(in_list):
        return -1
    else:
        return sum([in_list[start], in_list[start+1], in_list[start+2]])


def rolling_sum_increases(depth_measurements: List) -> int:
    current_index = 0
    prev_depth_sum = sum_three_safely(current_index, depth_measurements)
    count = 0
    for _ in depth_measurements:
        current_index += 1
        depth_avg = sum_three_safely(current_index, depth_measurements)
        if depth_avg != -1 and depth_avg > prev_depth_sum:
            count += 1
        prev_depth_sum = depth_avg

    return count
