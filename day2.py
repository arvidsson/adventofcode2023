import re

red, green, blue = 12, 13, 14

with open("day2.txt") as f:
    value = 0
    for line in f:
        game, *turns = re.split(r":|;", line.strip())
        result = [
            int(num) <= globals()[ball]
            for turn in turns
            for num, ball in (pair.split() for pair in re.split(r",", turn.strip()))
        ]
        if all(result):
            value += int(game.split()[1])
    print(value)
