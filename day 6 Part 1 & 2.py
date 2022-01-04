def ReadFile (name):
    with open(name, 'r') as data:
        return list(map(int, data.readlines()[0].split(",")))

# Day Six Problem One
def DayOne (fishes, days):
    for _ in range(days):
        for i in range(len(fishes)):
            if fishes[i] != 0:
                fishes[i] -= 1
            elif fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
    return len(fishes)

# Day Six **Problem Two
def DayTwo (name, days):
    fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(name, 'r') as data:
        for fish in data.read().split(","):
            fish_count[int(fish)] += 1

    for i in range(days):
        fish_count.append(fish_count.pop(0))
        fish_count[6] += fish_count[8]

    return sum(fish_count)
