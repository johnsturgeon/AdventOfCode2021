from typing import List, Optional


class Board:
    def __init__(self):
        self.rows: List[List] = []
        self.picked_numbers: List = []
        self.winning_sequence: List = []
        self.is_winner: bool = False

    def add_row(self, row: str):
        """ Expected Input 2 4 6 8 10"""
        row_list: List = row.split()
        self.rows.append(row_list)

    def is_complete(self):
        if len(self.rows) == 5:
            return True
        return False

    def get_winning_sequence(self, rows) -> Optional[List]:
        for row in rows:
            found = True
            for number in row:
                if number not in self.picked_numbers:
                    found = False
                    break
            if found:
                self.winning_sequence = row
                return row

    @property
    def columns(self) -> List:
        return list(zip(*self.rows[::-1]))

    def win_with_number_picked(self, picked_number) -> bool:
        self.picked_numbers.append(picked_number)
        if self.get_winning_sequence(self.rows):
            self.is_winner = True
        if self.get_winning_sequence(self.columns):
            self.is_winner = True
        return self.is_winner

    def sum_of_unpicked_numbers(self):
        sum_of_unpicked = 0
        for row in self.rows:
            for n in row:
                if n not in self.picked_numbers:
                    sum_of_unpicked += int(n)
        return sum_of_unpicked

    def final_score(self):
        last_number_picked: int = int(self.picked_numbers[-1])
        return self.sum_of_unpicked_numbers() * last_number_picked
