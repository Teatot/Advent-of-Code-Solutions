# Shoutout to https://www.youtube.com/channel/UCMhk437GeN8069t7y0lJQbw for the help on Part 1!


def ReadFile (name):
    with open(name, "r") as data:
        grid = []
        for line in data.readlines():
            grid.append([int(x) for x in line if x != "\n"])
    return grid



def add_grid(g, v):
    grid = [[x for x in range(len(g))] for _ in range(len(g[0]))]
    for r in range(len(g)):
        for c in range(len(g[r])):
            if g[r][c] + v > 9:
                grid[r][c] = (g[r][c] + v) - 9
            else:
                grid[r][c] = g[r][c] + v
    return grid

def add_row (r, v):
    row = [x for x in range(len(r))]
    for x in range(len(r)):
        if r[x] + v > 9:
            row[x] = (r[x] + v) - 9
        else:
            row[x] = r[x] + v
    return row



# Day 15 **Problem One
def DayOne (grid):
    path = [(0, 0, 0)]
    visited = set()
    maxx = len(grid)
    maxy = len(grid[0])

    while len(path) > 0:
        val, r, c = path.pop()

        if r == maxx - 1 and c == maxy - 1:
            return val

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            xr = r + x
            yc = c + y
            if 0 <= xr < maxx and 0 <= yc < maxy:
                # Queue
                path.append((val + grid[xr][yc], xr, yc))
                path = sorted(path, reverse=True)


# Day 15 Problem 2
def DayTwo (grid):
    grid = list(map(tuple, grid))
    maxx = len(grid) * 5
    maxy = len(grid[0]) * 5
    upd_grid = []

    # Update Row Length
    for v in {0, 1, 2, 3, 4}:
        g = add_grid(grid, v)
        upd_grid.extend(g)

    for r in range(maxx):
        lst = []
        for v in {1, 2, 3, 4}:
            lst.extend(add_row(upd_grid[r], v))
        upd_grid[r].extend(lst)

    # Finding the Path
    path = [(0, 0, 0)]
    visited = set()
    while len(path) > 0:
        val, r, c = path.pop()

        if r == maxx and c == maxy:
            return val

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for xr, yr in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr = xr + r
            cc = yr + c
            if 0 <= rr < maxx and 0 <= cc < maxy:
                path.append((val + upd_grid[rr][cc], rr, cc))
                path = sorted(path, reverse=True)
