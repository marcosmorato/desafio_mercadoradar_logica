r_positions = {"N": "E", "E": "S", "S": "W", "W": "N"}

l_positions = {"N": "W", "W": "S", "S": "E", "E": "N"}


def turn_left(pos: str):
    return l_positions[pos]


def turn_right(pos: str):
    return r_positions[pos]


def move(x: int, y: int, direction: str):

    if not y == 5 and direction == "N" or not y == -5 and direction == "S":
        y += 1 if direction == "N" else -1

    elif not x == 5 and direction == "E" or not x == -5 and direction == "W":
        x += 1 if direction == "E" else -1

    return [x, y, direction]
