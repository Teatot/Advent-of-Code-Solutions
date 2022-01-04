def ReadFile (name):
    with open(name, 'r') as data:
        l = ""
        for line in data.readlines():
            l += str(line)
    return l.split("\n")

# Day 2 Problem One
def DayOne (list):
    hor, dep = 0, 0
    for seq in list:
        seq = seq.split()
        if seq[0] == 'forward':
            hor += int(seq[1])
        elif seq[0] == 'up':
            dep -= int(seq[1])
        elif seq[0] == "down":
            dep += int(seq[1])
    return hor * dep

# Day 2 Problem Two
def DayTwo (list):
    hor, dep, aim = 0, 0, 0
    for seq in list:
        seq = seq.split()
        if seq[0] == 'forward':
            hor += int(seq[1])
            dep += (int(seq[1]) * aim)
        elif seq[0] == 'up':
            aim -= int(seq[1])
        elif seq[0] == "down":
            aim += int(seq[1])
    return hor * dep

print(DayOne(ReadFile("Data Files\\Solution Two Data")))
print(DayTwo(ReadFile("Data Files\\Solution Two Data")))