from typing import List

import pytest
import day01


@pytest.fixture
def sample_list() -> List:
    return [199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263]


@pytest.fixture
def real_list() -> List:
    filename = "test_data/day01.txt"
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(int(line))
    return real_list


def test_day_01_sample(sample_list):
    assert day01.number_increases(sample_list) == 7


def test_day_01(real_list):
    assert day01.number_increases(real_list) == 1215


def test_day_01_part_two_sample(sample_list):
    assert day01.rolling_sum_increases(sample_list) == 5


def test_day_01_part(real_list):
    assert day01.rolling_sum_increases(real_list) == 1150
