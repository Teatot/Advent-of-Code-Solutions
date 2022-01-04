def ReadFile (name):
    with open(name, 'r') as data:
        s = []
        for num in data.readlines():
            if num != '\n':
                s.append(int(num))
    return s

# Day 1 Problem One
def DayOne (list):
    incr = 0
    for i in range(1, len(list)):
        j = i - 1
        element = list[i]
        if element > list[j]:
            incr += 1
    return incr

# Day 1 Problem Two
def DayTwo (list):
    incr = 0
    a, b = 0, 3
    while b < len(list):
        sum_a = sum([list[i] for i in range(a, b)])
        sum_b = sum([list[i] for i in range(a + 1, b + 1)])
        if sum_b > sum_a:
            incr += 1
        a += 1
        b += 1
    return incr
