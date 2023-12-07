# NOT WORKING :(
import re


def get_matrix(input):
    m = []
    for i, line in enumerate(f):
        m.append([])
        for c in line.strip():
            m[i].append(c)
    return m


def get_positions(m):
    p = []
    for y, _ in enumerate(m):
        for x, c in enumerate(m[y]):
            if c != "." and not c.isdigit():
                p.append((x, y))
    return p


def get_numbers(m):
    n = []
    for row in m:
        num = ""
        for col in row:
            if col.isdigit():
                num += col
            else:
                if num != "":
                    n.append(int(num))
                    num = ""
    return n


def floodfill(m, pos):
    h = len(m)
    w = len(m[0])
    x, y = pos
    if m[y][x] == ".":
        return
    elif m[y][x] == "§":
        return
    m[y][x] = "§"
    neighbors = [
        (x - 1, y),
        (x + 1, y),
        (x - 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x, y - 1),
        (x, y + 1),
    ]
    for n in neighbors:
        if 0 <= n[0] <= w - 1 and 0 <= n[1] <= h - 1:
            floodfill(m, (n[0], n[1]))


with open("day3.txt") as f:
    m = get_matrix(f)
    n = get_numbers(m)
    p = get_positions(m)
    for x, y in p:
        floodfill(m, (x, y))
    s = get_numbers(m)
    print(sum(n) - sum(s))
    # for j in m:
    #     for i in j:
    #         print(i, end="")
    #     print("")
