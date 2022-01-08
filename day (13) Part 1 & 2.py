def ReadFile (name):
    points = []
    cmds = []
    with open(name, 'r') as data:
        for line in data.readlines():
            if len(line.split(",")) == 2:
                points.append([tuple(x.split(",")) for x in line.split()][0])
            elif len(line.split()) > 1:
                cmds.append(line.split()[-1])

    return points, cmds

# Returns the Max x and y values within a set of points
def max_xy (points):
    max_x, max_y = points[0]
    for point in points:
        x, y = point
        if int(x) > int(max_x):
            max_x = x
        if int(y) > int(max_y):
            max_y = y
    return int(max_y), int(max_x)

# Creates a grid that has 'x' rows and 'y' columns
def make_grid (x, y):
    grid = []
    for _ in range(x + 1):
        row = []
        for _ in range(y + 1):
            row.append(".")
        grid.append(row)
    return grid

def split_paper (paper, line):
    # Fold at x
    if line.split("=")[0] == 'y':
        y_fold = int(line.split("=")[1])
        for r in range(len(paper[0])):
            for c in range(y_fold + 1, len(paper)):
                if paper[c][r] == "#" and paper[y_fold - abs(c - y_fold)][r] == ".":
                    paper[y_fold - abs(c - y_fold)][r] = "#"
        return paper[:y_fold] # Folding Process (Vertically)
    # Fold at y
    else:
        x_fold = int(line.split("=")[1])
        for r in range(x_fold + 1, len(paper[0])):
            for c in range(len(paper)):
                if paper[c][r] == "#" and paper[c][x_fold - abs(r - x_fold)] == ".":
                    paper[c][x_fold - abs(r - x_fold)] = "#"
        # Folding Process (Horizontally)
        for i in range(len(paper)):
            paper[i] = paper[i][:x_fold]
        return paper

# Finds the amount of dots within the grid
def dots_squares (grid):
    dots = 0
    for row in grid:
        for sq in row:
            if sq == "#":
                dots += 1
    return dots

# Day 13 Problem One
def DayOne (points, cmds):
    paper = make_grid(*max_xy(points))
    for point in points:
        x, y = point
        paper[int(y)][int(x)] = "#"
    paper = split_paper(paper, cmds[0])
    return dots_squares(paper)

# Day 13 Problem Two
def DayTwo (points, cmds):
    paper = make_grid(*max_xy(points))
    for point in points:
        x, y = point
        paper[int(y)][int(x)] = "#"
    for inst in cmds:
        paper = split_paper(paper, inst)
    for i in paper:
        print(i)
