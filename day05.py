from typing import List


class ThermalVent:
    def __init__(self, start: List, end: List):
        """ Pairs area a list of two [x,y] """
        self.start_coordinate: List = [int(start[0]), int(start[1])]
        self.end_coordinate: List = [int(end[0]), int(end[1])]
        self.start_x: int = self.start_coordinate[0]
        self.start_y = self.start_coordinate[1]
        self.end_x: int = self.end_coordinate[0]
        self.end_y = self.end_coordinate[1]

    @property
    def is_horizontal(self) -> bool:
        return self.start_y == self.end_y

    @property
    def is_vertical(self) -> bool:
        return self.start_x == self.end_x

    @property
    def is_diagonal(self) -> bool:
        if not self.is_horizontal and not self.is_vertical:
            return True

    @property
    def min_x(self) -> int:
        return min(self.start_x, self.end_x)

    @property
    def max_x(self) -> int:
        return max(self.start_x, self.end_x)

    @property
    def min_y(self) -> int:
        return min(self.start_y, self.end_y)

    @property
    def max_y(self) -> int:
        return max(self.start_y, self.end_y)

    def __str__(self):
        description: str = f"Start x: {self.start_x} y: {self.start_y}\n"
        description += f"End x: {self.end_x} y: {self.end_y}\n"
        description += f"Is Horizontal: {self.is_horizontal}\n"

        return description

    def list_of_coordinate_keys(self, use_diagonal=False) -> List[str]:
        """ Return a list of points ['0,1','0,2','0,3']
        :param use_diagonal:
        """
        return_list: List = []
        if self.is_horizontal:
            x_points: List[int] = []
            for i in range(self.min_x, self.max_x+1):
                x_points.append(i)
            for point in x_points:
                return_list.append(f"{point},{self.start_y}")
        elif self.is_vertical:
            y_points: List[int] = []
            for i in range(self.min_y, self.max_y+1):
                y_points.append(i)
            for point in y_points:
                return_list.append(f"{self.start_x},{point}")
        elif use_diagonal and self.is_diagonal:
            # {4,4} {2,2}
            y_points: List[int] = []
            y_increment: int = 1 if self.start_y < self.end_y else -1
            for y in range(self.start_y, self.end_y + y_increment, y_increment):
                y_points.append(y)
            x_points: List[int] = []
            x_increment: int = 1 if self.start_x < self.end_x else -1
            for x in range(self.start_x, self.end_x + x_increment, x_increment):
                x_points.append(x)
            for i in range(len(y_points)):
                return_list.append(f"{x_points[i]},{y_points[i]}")

        return return_list


def count_multiples(thermal_vents: List[ThermalVent], use_diagonals=False) -> int:
    all_coordinates: dict = {}
    multiple_count: int = 0
    for vent in thermal_vents:
        for key in vent.list_of_coordinate_keys(use_diagonals):
            if key not in all_coordinates:
                all_coordinates[key] = 0
            all_coordinates[key] += 1

    for key, value in all_coordinates.items():
        if value > 1:
            multiple_count += 1
    return multiple_count



