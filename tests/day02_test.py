from typing import List

import pytest
import day02


@pytest.fixture
def sample_list() -> List:
    return ['forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2']


@pytest.fixture
def real_list() -> List:
    filename = "test_data/day02.txt"
    real_list = []
    with open(filename, 'r', encoding='utf8') as file_handle:
        for line in file_handle:
            real_list.append(line)
    return real_list


def test_day_02_sample(sample_list):
    assert day02.position_multiplied(sample_list) == 150


def test_day_02(real_list):
    assert day02.position_multiplied(real_list) == 1938402


def test_day_02_part_2_sample(sample_list):
    assert day02.position_multiplied_02(sample_list) == 900


def test_day_02_part_2(real_list):
    assert day02.position_multiplied_02(real_list) == 1947878632

