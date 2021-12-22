from typing import List

import pytest
from day04 import Board


@pytest.fixture
def sample_input() -> List[int]:
    filename = "test_data/day04_sample_input.txt"
    number_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            number_list = line.split(',')
    return number_list


@pytest.fixture
def sample_boards() -> List[Board]:

    filename = "test_data/day04_sample_boards.txt"
    sample_boards = []
    board: Board = Board()
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            if len(line) > 2:
                board.add_row(line)
                if board.is_complete():
                    sample_boards.append(board)
                    board: Board = Board()

    return sample_boards


@pytest.fixture
def real_input() -> List[int]:
    filename = "test_data/day04_input.txt"
    number_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            number_list = line.split(',')
    return number_list


@pytest.fixture
def real_boards() -> List[Board]:
    filename = "test_data/day04_boards.txt"
    boards = []
    board: Board = Board()
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            if len(line) > 2:
                board.add_row(line)
                if board.is_complete():
                    boards.append(board)
                    board: Board = Board()

    return boards


def test_get_sample_boards(sample_boards, sample_input):
    board: Board
    for number in sample_input:
        for board in sample_boards:
            if board.win_with_number_picked(number):
                assert board.final_score() == 4512
                return


def test_get_board(real_boards, real_input):
    board: Board
    for number in real_input:
        for board in real_boards:
            if board.win_with_number_picked(number):
                assert board.final_score() == 6592
                return


def test_get_last_board(real_boards, real_input):
    board: Board
    last_winning_board: Board = None
    for number in real_input:
        for board in real_boards:
            if not board.is_winner and board.win_with_number_picked(number):
                last_winning_board = board
    assert last_winning_board.final_score() == 31755
