import re

red = 12
green = 13
blue = 14

with open("day2.txt") as f:
    value = 0
    for line in f:
        valid = True
        game = re.split(r":", line)
        index = int(game[0].split()[1])
        result = re.split(r";", game[1])
        for part in result:
            balls = re.split(r",", part)
            for ball in balls:
                ball = ball.split()
                num = int(ball[0])
                btype = ball[1]
                if btype == "red":
                    if num > red:
                        valid = False
                elif btype == "green":
                    if num > green:
                        valid = False
                elif btype == "blue":
                    if num > blue:
                        valid = False
        if valid is True:
            value += index
    print(value)
