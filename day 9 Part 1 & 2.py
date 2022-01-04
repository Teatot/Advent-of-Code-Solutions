def ReadFile (name):
    grid = []
    with open (name, 'r') as data:
        for line in data.readlines():
            grid.append([x for x in line if x != '\n'])
    return grid

# If the given point is a low point
def is_low_point (grid, x, y):
    t = 0
    if (x + 1) in range(len(grid)) and grid[x][y] < grid[x + 1][y]:
        t += 1
    if (x - 1) in range(len(grid)) and grid[x][y] < grid[x - 1][y]:
        t += 1
    if (y + 1) in range(len(grid[x])) and grid[x][y] < grid[x][y + 1]:
        t += 1
    if (y - 1) in range(len(grid[x])) and grid[x][y] < grid[x][y - 1]:
        t += 1
    if t == 4:
        return True
    elif t == 3 and (x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[x]) - 1):
        return True
    elif t == 2 and (x == 0 or x == len(grid) - 1) and (y == 0 or y == len(grid[x]) - 1):
        return True
    return False

# Recursive Function that searches around the low point to find a Basin
def SearchBasin (grid, seen, x, y):
    # Base Cases
    if (x, y) in seen:
        return

    if x > len(grid) - 1 or y > len(grid[x]) - 1 or x < 0 or y < 0:
        return

    if int(grid[x][y]) == 9:
        return

    seen.append((x, y))
    # Moving Down
    SearchBasin(grid, seen, x + 1, y)

    # Moving Up
    SearchBasin(grid, seen, x - 1, y)

    # Moving Left
    SearchBasin(grid, seen, x, y - 1)

    # Moving Right
    SearchBasin(grid, seen, x, y + 1)


# Day 9 Problem One
def DayOne (grid):
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            t = 0
            if (x + 1) in range(len(grid)) and grid[x][y] < grid[x + 1][y]:
                t += 1
            if (x - 1) in range(len(grid)) and grid[x][y] < grid[x - 1][y]:
                t += 1
            if (y + 1) in range(len(grid[x])) and grid[x][y] < grid[x][y + 1]:
                t += 1
            if (y - 1) in range(len(grid[x])) and grid[x][y] < grid[x][y - 1]:
                t += 1
            if t == 4:
                total += int(grid[x][y]) + 1
            elif t == 3 and (x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[x]) - 1):
                total += int(grid[x][y]) + 1
            elif t == 2 and (x == 0 or x == len(grid) - 1) and (y == 0 or y == len(grid[x]) - 1):
                total += int(grid[x][y]) + 1
    return total


# Day 9 **Problem Two
def DayTwo(grid):
    rasins = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if is_low_point(grid, x, y):
                pos = []
                SearchBasin(grid, pos, x, y)
                rasins.append(len(pos))
    rasins = sorted(rasins)
    rasins = rasins[::-1]
    return rasins[0] * rasins[1] * rasins[2]
