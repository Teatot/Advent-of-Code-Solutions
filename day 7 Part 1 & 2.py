# Based on the midpoint, determines which side is more densely populated
def Density_Check (center, coords):
    big, small = 0, 0
    for val in coords:
        if center > val:
            small += 1
        elif center < val:
            big += 1
    return True if big > small else False


# Day Seven Problem One
def DayOne (name):
    with open(name, 'r') as data:
        positions = [int(x) for x in data.read().split(",")]

    fuels = []
    cen = round((max(positions) + min(positions))/2)
    if Density_Check(cen, positions):
        start = cen
        end = max(positions)
    else:
        start = min(positions) + 1
        end = cen + 1
    for pos in range(start, end):
        f = 0
        for val in positions:
            f += abs(pos - val)
        fuels.append(f)
    return min(fuels)

# Day 7 Problem Two
def DayTwo (name):
    with open(name, 'r') as data:
        positions = [int(x) for x in data.read().split(",")]

    fuels = []
    cen = round((max(positions) + min(positions))/2)
    if Density_Check(cen, positions):
        start = cen
        end = max(positions)
    else:
        start = min(positions) + 1
        end = cen + 1
    for pos in range(start, end):
        f = 0
        for val in positions:
            f += sum(list(range(1, abs(pos - val) + 1)))
        fuels.append(f)
    return min(fuels)
