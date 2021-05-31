from services.commands import turn_left, turn_right, move


def robo(commands: str):
    pos = [0, 0, "N"]

    for cmd in commands:
        if cmd == "L":
            pos[2] = turn_left(pos[2])

        elif cmd == "R":
            pos[2] = turn_right(pos[2])

        elif cmd == "M":
            pos = move(pos[0], pos[1], pos[2])

    return pos
