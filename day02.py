from typing import List


def position_multiplied(movement: List):
    h_position = 0
    depth = 0
    move: str
    for move in movement:
        distance: int
        direction = move.split()[0]
        distance = int(move.split()[1])
        match direction:
            case 'forward':
                h_position += distance
            case 'down':
                depth += distance
            case 'up':
                depth -= distance
    return h_position * depth


def position_multiplied_02(movement: List):
    aim = 0
    h_position = 0
    depth = 0
    move: str
    for move in movement:
        distance: int
        direction = move.split()[0]
        distance = int(move.split()[1])
        match direction:
            case 'forward':
                h_position += distance
                depth += distance * aim
            case 'down':
                aim += distance
            case 'up':
                aim -= distance
    return h_position * depth
