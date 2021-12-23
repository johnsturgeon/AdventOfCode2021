from typing import List

import pytest
from day05 import ThermalVent
import day05


@pytest.fixture
def sample_input() -> List[ThermalVent]:
    filename = "test_data/day05_sample_input.txt"
    thermal_vents: List[ThermalVent] = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            if len(line) > 1:
                chomped_line = line.rstrip()
                start_pair, end_pair = chomped_line.split(' -> ')
                new_vent: ThermalVent = ThermalVent(
                    start_pair.split(','), end_pair.split(','))
                thermal_vents.append(new_vent)
    return thermal_vents


@pytest.fixture
def real_input() -> List[ThermalVent]:
    filename = "test_data/day05.txt"
    thermal_vents: List[ThermalVent] = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            if len(line) > 1:
                chomped_line = line.rstrip()
                start_pair, end_pair = chomped_line.split(' -> ')
                new_vent: ThermalVent = ThermalVent(
                    start_pair.split(','), end_pair.split(','))
                thermal_vents.append(new_vent)
    return thermal_vents


def test_sample_thermal_vent_navigation(sample_input):
    assert day05.count_multiples(sample_input) == 5


def test_sample_thermal_vent_navigation_diags(sample_input):
    assert day05.count_multiples(sample_input, use_diagonals=True) == 12


def test_thermal_vent_navigation(real_input):
    assert day05.count_multiples(real_input) == 6007


def test_thermal_vent_navigation_diags(real_input):
    assert day05.count_multiples(real_input, use_diagonals=True) == 19349
