def ReadFile (name):
    with open (name, 'r') as data:
        coords = []
        for line in data.readlines():
            l = []
            for x in line.split():
                if x != "->":
                    l.append(x)
            coords.append(l)
    return coords


# Creates the grid; based on the max x and y
def Grid_Maker (lg_x, lg_y):
    grid = []
    for _ in range(lg_x):
        row = []
        for _ in range(lg_y):
            row.append(".")
        grid.append(row)
    return grid

# Returns the Largest x, y values of the coordinates
def Largest (coords):
    x, y = 0, 0
    for set in coords:
        for val in set:
            a, b = val.split(",")
            if x == 0 and y == 0:
                x = a
                y = b
            else:
                if int(x) < int(a):
                    x = int(a)
                elif int(y) < int(b):
                    y = int(b)
    return x, y

# Applying the line based on the points
def Apply_Line (points, grid):
    for point in points:
        a, b = point
        if grid[a][b] == ".":
            grid[a][b] = 1
        else:
            grid[a][b] += 1
    return grid

# Calculates the number of intersections >=2
def Intersection (grid):
    num = 0
    for row in grid:
        for val in row:
            if type(val) is int:
                if val >= 2:
                    num += 1
    return num


# Day Five Problem One
def DayOne (coords):
    max_x, max_y = Largest(coords)
    grid = Grid_Maker(int(max_x) + 1, int(max_y) + 1)
    for set in coords:
        points = []
        a, b = set
        a, b = list(map(int, a.split(","))), list(map(int, b.split(",")))
        if a[0] == b[0]:
            lwt = b[1] if b[1] < a[1] else a[1]
            for i in range(abs(b[1] - a[1]) + 1):
                points.append((a[0], lwt + i))
        elif a[1] == b[1]:
            lwt = b[0] if b[0] < a[0] else a[0]
            for i in range(abs(b[0] - a[0]) + 1):
                points.append((lwt + i, a[1]))
        grid = Apply_Line(points, grid)
    return Intersection(grid)

# Day Five Problem Two
def DayTwo (coords):
    max_x, max_y = Largest(coords)
    grid = Grid_Maker(int(max_x) + 1, int(max_y) + 1)
    for set in coords:
        points = []
        a, b = set
        a, b = list(map(int, a.split(","))), list(map(int, b.split(",")))
        if a[0] == b[0]:
            lwt = b[1] if b[1] < a[1] else a[1]
            for i in range(abs(b[1] - a[1]) + 1):
                points.append((a[0], lwt + i))
        elif a[1] == b[1]:
            lwt = b[0] if b[0] < a[0] else a[0]
            for i in range(abs(b[0] - a[0]) + 1):
                points.append((lwt + i, a[1]))
        elif abs(a[1] - b[1]) == abs(a[0] - b[0]):
            if b[1] >= a[1] and b[0] >= a[0]:
                for i in range(abs(a[1] - b[1]) + 1):
                    points.append((a[0] + i, a[1] + i))
            elif a[1] > b[1] and b[0] >= a[0]:
                for i in range(abs(a[1] - b[1]) + 1):
                    points.append((a[0] + i, a[1] - i))
            elif a[0] > b[0] and b[1] >= a[1]:
                for i in range(abs(a[1] - b[1]) + 1):
                    points.append((a[0] - i, a[1] + i))
            elif a[1] > b[1] and a[0] > b[0]:
                for i in range(abs(a[1] - b[1]) + 1):
                    points.append((a[0] - i, a[1] - i))
        grid = Apply_Line(points, grid)
    return Intersection(grid)
