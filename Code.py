def LowestPoint (grid, x, y):
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

def SearchBasin (grid, positions, x, y):
    # Base Cases
    if (x, y) in positions:
        return positions

    if x > len(grid) - 1 or y > len(grid[x]) - 1:
        return None

    if not LowestPoint(grid, x, y):
        return None

    # Moving Up
    print("Up")
    positions.append((x + 1, y))
    p_up = SearchBasin(grid, positions, x + 1, y)
    if p_up is not None:
        return p_up

    # Moving Down
    print("Down")
    positions.pop()
    positions.append((x - 1, y))
    p_down = SearchBasin(grid, positions, x - 1, y)
    if p_down is not None:
        return p_down

    # Moving Left
    print("Left")
    positions.pop()
    positions.append((x, y - 1))
    p_left = SearchBasin(grid, positions, x, y - 1)
    if p_left is not None:
        return p_left

    # Moving Right
    print("Right")
    positions.pop()
    positions.append((x, y + 1))
    p_right = SearchBasin(grid, positions, x, y + 1)
    if p_right is not None:
        return p_right

    positions.pop()
    return None

def sol18 (grid):
    rasins = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            pos = []

            SearchBasin(grid, pos, x, y)
            rasins.append(pos)
    return rasins

