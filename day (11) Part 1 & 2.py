def ReadFile (name):
    with open(name, 'r') as data:
        arr = []
        for line in data.read().split():
            arr.append([int(x) for x in line])
    return arr


# Checks the surrounding and adds one to the surrounding of the position
def Add_Surrounding (grid, r, c, vals):
    # Corners
    if (r, c) in ((0, 0), (0, len(grid[r]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[r]) - 1)):
        # if (r, c) == (len(grid) - 1, len(grid[r]) - 1)
        x1, x2, x3 = r - 1, r, r - 1
        y1, y2, y3 = c - 1, c - 1, c
        if (r, c) == (0, 0):
            x1, x2, x3 = r, r + 1, r + 1
            y1, y2, y3 = c + 1, c + 1, c
        elif (r, c) == (0, len(grid[r]) - 1):
            x1, x2, x3 = r, r + 1, r + 1
            y1, y2, y3 = c - 1, c - 1, c
        elif (r, c) == (len(grid) - 1, 0):
            x1, x2, x3 = r - 1, r, r - 1
            y1, y2, y3 = c, c + 1, c + 1
        grid[r][c] = 0
        grid[x1][y1] = grid[x1][y1] + 1 if (x1, y1) not in vals else 0
        grid[x2][y2] = grid[x2][y2] + 1 if (x2, y2) not in vals else 0
        grid[x3][y3] = grid[x3][y3] + 1 if (x3, y3) not in vals else 0
    # Edges
    elif r in (0, len(grid) - 1) or c in (0, len(grid) - 1):
        # if r == 0
        x1, x2, x3, x4, x5 = r, r, r + 1, r + 1, r + 1
        y1, y2, y3, y4, y5 = c - 1, c + 1, c - 1, c, c + 1
        if c == 0:
            x1, x2, x3, x4, x5 = r - 1, r + 1, r - 1, r, r + 1
            y1, y2, y3, y4, y5 = c, c, c + 1, c + 1, c + 1
        elif r == len(grid) - 1:
            x1, x2, x3, x4, x5 = r, r, r - 1, r - 1, r - 1
            y1, y2, y3, y4, y5 = c - 1, c + 1, c - 1, c, c + 1
        elif c == len(grid) - 1:
            x1, x2, x3, x4, x5 = r - 1, r + 1, r - 1, r, r + 1
            y1, y2, y3, y4, y5 = c, c, c - 1, c - 1, c - 1
        grid[r][c] = 0
        grid[x1][y1] = grid[x1][y1] + 1 if (x1, y1) not in vals else 0
        grid[x2][y2] = grid[x2][y2] + 1 if (x2, y2) not in vals else 0
        grid[x3][y3] = grid[x3][y3] + 1 if (x3, y3) not in vals else 0
        grid[x4][y4] = grid[x4][y4] + 1 if (x4, y4) not in vals else 0
        grid[x5][y5] = grid[x5][y5] + 1 if (x5, y5) not in vals else 0

    else:
        grid[r][c] = 0
        grid[r - 1][c - 1] = grid[r - 1][c - 1] + 1 if (r - 1, c - 1) not in vals else 0  # Top Left
        grid[r][c - 1] = grid[r][c - 1] + 1 if (r, c - 1) not in vals else 0  # Middle Left
        grid[r + 1][c - 1] = grid[r + 1][c - 1] + 1 if (r + 1, c - 1) not in vals else 0  # Bottom Left
        grid[r + 1][c] = grid[r + 1][c] + 1 if (r + 1, c) not in vals else 0  # Bottom Middle
        grid[r - 1][c] = grid[r - 1][c] + 1 if (r - 1, c) not in vals else 0  # Top Middle
        grid[r + 1][c + 1] = grid[r + 1][c + 1] + 1 if (r + 1, c + 1) not in vals else 0  # Bottom Right
        grid[r][c + 1] = grid[r][c + 1] + 1 if (r, c + 1) not in vals else 0  # Middle Right
        grid[r - 1][c + 1] = grid[r - 1][c + 1] + 1 if (r - 1, c + 1) not in vals else 0  # Top Right

# Checks if a position is >9
def is_nine (grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] > 9:
                return True
    return False

# Checks how many flashes had occurred and returns the amount
def Check_Flashes (grid):
    vals = []
    score = 0
    while is_nine(grid):
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > 9:
                    score += 1
                    vals.append((r,c))
                    Add_Surrounding(grid, r, c, vals)
    return score


# Day Eleven Problem One
def DayOne (grid, days):
    flashes = 0
    for _ in range(days):
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                grid[r][c] += 1
        flashes += Check_Flashes(grid)
    return flashes

# Day Eleven Problem Two
def DayTwo (grid):
    steps = 0
    while True:
        steps += 1
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                grid[r][c] += 1
        if Check_Flashes(grid) == (len(grid) * len(grid[0])):
            return steps

