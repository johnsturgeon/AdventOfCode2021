from typing import List


class LanternFish:
    def __init__(self, start_age):
        self.start_age: int = start_age
        self.days_alive: int = 18
        self.children: List[LanternFish]

    def kids(self, days):
        days -= self.start_age
        if days <= 0:
            return 0
        children, _ = divmod(days, 8)
        return pow(2, children)


def children_for_days(days_to_propagate: int, days_to_mature: int) -> int:
    # first, answer the question.. how many children will I have given the days to propagate
    # subtracting my days_to_mature
    total_days_to_propagate: int = days_to_propagate - (days_to_mature + 1)
    number_of_children, _ = divmod(total_days_to_propagate, 7)
    grand_children: int = 0
    if days_to_mature < days_to_propagate:
        number_of_children += 1
    number_of_children = max(0, number_of_children)
    if number_of_children > 0:
        for child in range(number_of_children):
            number_of_children += children_for_days(total_days_to_propagate, 8)
    return number_of_children


def test_children_for_days():
    print("\n")
    for i in range(18):
        print(f"Day: {i+1}: ", end="")
        print(children_for_days(i+1, 4))

