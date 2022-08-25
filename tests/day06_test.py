from typing import List

import pytest
from day06 import LanternFish
import day06


@pytest.fixture
def sample_input() -> List[int]:
    filename = "test_data/day06_sample.txt"
    sample_list: List = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            if len(line) > 2:
                chomped_line = line.rstrip()
                for item in chomped_line.split(','):
                    sample_list.append(int(item))

    return sample_list


def test_sample(sample_input: List[int]):
    total_fish: int = len(sample_input)
    print('\n')
    for num in sample_input:
        total_fish += day06.children_for_days(11, num)
    print('\n' + str(total_fish))