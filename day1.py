with open("day1.txt") as f:
    value = 0
    for line in f:
        first = "0"
        last = "0"
        for c in line:
            if c.isdigit():
                if first == "0":
                    first = c
                else:
                    last = c
        if last == "0":
            last = first
        num = int(first + last)
        value += num
    print(value)
