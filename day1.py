import re

with open("day1.txt") as f:
    value = 0
    for line in f:
        digits = re.findall("\d", line)
        first = digits[0]
        last = digits[len(digits) - 1]
        num = int(first + last)
        value += num
    print(value)
