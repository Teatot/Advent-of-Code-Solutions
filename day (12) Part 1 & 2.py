def ReadFile (name):
    connections = []
    caves = []
    assignment = {}
    with open(name, 'r') as data:
        for line in data.read().split():
            connections.append(line.split("-"))
            caves.extend(line.split("-"))
    for cave in set(caves):
        connected_caves = []
        if cave != 'end':
            for connect in connections:
                if cave in connect:
                    p = connect[0] if connect[0] != cave else connect[1]
                    connected_caves.append(p)
            assignment[cave] = [x for x in connected_caves if x != "start"]
    return assignment

# Recursive function for part one
def enter_cave_pt1 (map, path, routes):
    if path[-1] == "end":
        routes.append(tuple(path))
        return

    for cave in map[path[-1]]:
        if (cave.isupper()) or (cave not in path):
            path.append(cave)
            enter_cave_pt1(map, path, routes)
            path.pop()

# Return an integer that tells how many times the "symbol" is in the array
def visited_cave (cave, sym):
    times = 0
    for amt in cave:
        if amt == sym:
            times += 1
    return times

# Recursive function for part two
def enter_cave_pt2 (map, path, routes, visited_twice):
    if path[-1] == "end":
        routes.append(tuple(path))
        return

    for cave in map[path[-1]]:
        if (cave.isupper()) or (cave not in path):
            path.append(cave)
            enter_cave_pt2(map, path, routes, visited_twice)
            path.pop()
        elif cave.islower() and visited_twice == "":
            if visited_cave(path.copy(), cave) <= 1:
                visited_twice = cave
                path.append(cave)
                enter_cave_pt2(map, path, routes, visited_twice)
                path.pop()
                visited_twice = ""

# Day Twelve **Problem One
def DayOne (cave_map):
    sol = []
    path = ["start"]
    enter_cave_pt1(cave_map, path, sol)
    return len(sol)

# Day Twelve Problem Two
def DayTwo (cave_map):
    sol = []
    twice = ""
    path = ["start"]
    enter_cave_pt2(cave_map, path, sol, twice)
    return len(sol)
