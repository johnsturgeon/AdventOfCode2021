from typing import List

import pytest
import day03


@pytest.fixture
def sample_list() -> List:
    return ['00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010']


@pytest.fixture
def real_list() -> List:
    filename = "test_data/day03.txt"
    real_list = []
    with open(filename, 'r', encoding='utf8') as file_handle:
        for line in file_handle:
            real_list.append(line.rstrip())
    return real_list


def test_day_03_sample(sample_list):
    assert day03.power_consumption(sample_list) == 198


def test_day_03(real_list):
    assert day03.power_consumption(real_list) == 4191876


def test_day_03_part_2_sample(sample_list):
    assert day03.get_diagnostic_rating(False, sample_list) == 23
    assert day03.get_diagnostic_rating(True, sample_list) == 10
    assert day03.get_life_support_rating(sample_list) == 230


def test_day_03_part_2(real_list):
    assert day03.get_life_support_rating(real_list) == 3414905
