def FileReadDayOne (name):
    with open(name, 'r') as data:
        s = []
        for num in data.readlines():
            if num != '\n':
                s.append(int(num))
    return s

def FileReadDayTwo (name):
    with open(name, 'r') as data:
        l = ""
        for line in data.readlines():
            l += str(line)
    return l.split("\n")

def FileReadDayFour (name):
    with open(name, 'r') as data:
        counter = 0
        boards, e = [], []
        nums = 1
        for board in data.readlines():
            if nums == 1:
                nums = list(map(int, board.split(",")))
            elif len(board.split()) > 0 and counter < 5:
                vector = list(map(int, board.split()))
                e.append(vector)
                counter += 1
            elif counter == 5:
                boards.append(e)
                counter = 0
                e = []
    return nums, boards

def FileReadDayFive (name):
    with open (name, 'r') as data:
        coords = []
        for line in data.readlines():
            l = []
            for x in line.split():
                if x != "->":
                    l.append(x)
            coords.append(l)
    return coords

def FileReadDaySix (name):
    with open(name, 'r') as data:
        return list(map(int, data.readlines()[0].split(",")))

def FileReadDayEight(name):
    segments = []
    with open(name, 'r') as data:
        codes = data.read().split("\n")
        for c in codes:
            segments.append(c.split("|"))
    return segments


# Day 1 Problem One
def sol1 (list):
    incr = 0
    print(list)
    for i in range(1, len(list)):
        j = i - 1
        element = list[i]
        if element > list[j]:
            incr += 1
    return incr

# Day 1 Problem Two
def sol2 (list):
    incr = 0
    a, b = 0, 3
    while b < len(list):
        sum_a = sum([list[i] for i in range(a, b)])
        sum_b = sum([list[i] for i in range(a + 1, b + 1)])
        if sum_b - sum_a > 0:
            incr += 1
        a += 1
        b += 1
    return incr

# Day 2 Problem One
def sol3 (list):
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
def sol4 (list):
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


# Day 3 Problem One
def sol5 (list):
    most, least = "", ""
    for i in range(len(list[0])):
        on, off = 0, 0
        for bin in list:
            if bin[i] == '1':
                on += 1
            else:
                off += 1
        if on > off:
            most += '1'
        else:
            most += '0'
    for n in most:
        if n == '1':
            least += '0'
        else:
            least += '1'
    return int(most, 2) * int(least, 2)

# Day 3 Problem Two
def Freq (list, place):
    on, off = 0,0
    for bin in list:
        if bin[place] == '1':
            on += 1
        else:
            off += 1
    if on > off:
        return '1'
    elif off > on:
        return '0'
    else:
        return '-1'

def LessFreq (list, place):
    on, off = 0, 0
    for bin in list:
        if bin[place] == '1':
            on += 1
        else:
            off += 1
    if on < off:
        return '1'
    elif off < on:
        return '0'
    else:
        return '-1'

def sol6 (list):
    o, c = list, list
    for i in range(len(list[0])):
        if len(o) > 1:
            pop_o = Freq(o, i)
            if pop_o == '0':
                o = [x for x in o if x[i] == "0"]
            elif pop_o == '1' or pop_o == '-1':
                o = [x for x in o if x[i] == "1"]
        if len(c) > 1:
            pop_c = LessFreq(c, i)
            if pop_c == '1':
                c = [x for x in c if x[i] == '1']
            elif pop_c == '0' or pop_c == '-1':
                c = [x for x in c if x[i] == "0"]
    return int(o[0], 2) * int(c[0], 2)

# Day 4 Problem One
def Mark (board, num):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == num:
                board[r][c] = "X"
    return board

def Bingo (board):
    # Horizontal
    for r in range(len(board)):
        const = 0
        for c in range(len(board[0])):
            if board[r][c] == "X":
                const += 1
        if const == len(board[0]):
            return True
    # Vertical
    for c in range(len(board[0])):
        const = 0
        for r in range(len(board)):
            if board[r][c] == "X":
                const += 1
        if const == len(board):
            return True
    return False

def CalculateSum (board):
    sum = 0
    for row in board:
        for num in row:
            if type(num) is int:
                sum += num
    return sum

def sol7 (boards, nums):
    for num in nums:
        for board in boards:
            board = Mark(board, num)
            if Bingo(board):
                return CalculateSum(board) * num

# Day 4 Problem Two
def sol8 (boards, nums):
    solved = 0
    solved_b = []
    for num in nums:
        for ind in range(len(boards)):
            if ind not in solved_b:
                boards[ind] = Mark(boards[ind], num)
                if Bingo(boards[ind]):
                    if solved == len(boards) - 1:
                        print(f"Solved: {solved}\nBoards: {len(boards)}")
                        return CalculateSum(boards[ind]) * num
                    else:
                        solved += 1
                        solved_b.append(ind)

# Day Five Problem One
def Grid_Maker (lg_x, lg_y):
    grid = []
    for _ in range(lg_x):
        row = []
        for _ in range(lg_y):
            row.append(".")
        grid.append(row)
    return grid

def large_small (coords):
    x, y = [], []
    for set in coords:
        for val in set:
            a, b = val.split(",")
            if len(x) == 0 and len(y) == 0:
                x = [a, a]
                y = [b, b]
            else:
                if int(x[0]) > int(a):
                    x[0] = int(a)
                elif int(x[1]) < int(a):
                    x[1] = int(a)
                if int(y[0]) > int(b):
                    y[0] = int(b)
                elif int(y[1]) < int(b):
                    y[1] = int(b)
    return x[1], y[1]

def Apply_Line (points, grid):
    for point in points:
        a, b = point
        if grid[a][b] == ".":
            grid[a][b] = 1
        else:
            grid[a][b] += 1
    return grid

def Intersection (grid):
    num = 0
    for row in grid:
        for val in row:
            if type(val) is int:
                if val >= 2:
                    num += 1
    return num

def sol9 (coords):
    max_x, max_y = large_small(coords)
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
def sol10 (coords):
    max_x, max_y = large_small(coords)
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

# Day Six Problem One
def sol11 (fishes, days):
    for _ in range(days):
        for i in range(len(fishes)):
            if fishes[i] != 0:
                fishes[i] -= 1
            elif fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
    return len(fishes)

# Day Six Problem Two
def sol12 (days):
    fish_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open("Solution Six Data", 'r') as data:
        for fish in data.read().split(","):
            fish_count[int(fish)] += 1

    for i in range(days):
        fish_count.append(fish_count.pop(0))
        fish_count[6] += fish_count[8]

    return sum(fish_count)


# Day Seven Problem One
def Density_Check (center, coords):
    big, small = 0, 0
    for val in coords:
        if center > val:
            small += 1
        elif center < val:
            big += 1
    return True if big > small else False

def sol13 ():
    with open("Solution Seven Data", 'r') as data:
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
def sol14 ():
    with open("Solution Seven Data", 'r') as data:
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

# Day 8 Problem One
def sol15 (codes):
    total = 0
    for segment in codes:
        for code in segment[1].split():
            if len(code) in (2, 3, 4, 7):
                total += 1
    return total

# Day 8 Problem Two
def CommonChars (a, b):
    common = 0
    for i in a:
        for j in b:
            if i == j:
                common += 1
    return common

def DecodeMessage (message, ref):
    line = ""
    for code in message:
        for i in range(10):
            if sorted(code) == sorted(ref[i]):
                line += str(i)
                break
    return int(line)

def sol16 (codes):
    total = 0
    for segment in codes:
        key = {}
        others = [x for x in segment[0].split() if len(x) in (2, 3, 4, 7)]
        fives = [x for x in segment[0].split() if len(x) == 5]
        sixes = [x for x in segment[0].split() if len(x) == 6]

        # 1, 4, 7 and 8
        for sym in others:
            if len(sym) == 2:
                key[1] = sym
            elif len(sym) == 3:
                key[7] = sym
            elif len(sym) == 4:
                key[4] = sym
            else:
                key[8] = sym

        # 2, 3, 5
        for sym in fives:
            if CommonChars(key[1], sym) == 2:
                key[3] = sym
            elif CommonChars(key[4], sym) == 3:
                key[5] = sym
            elif CommonChars(key[4], sym) == 2:
                key[2] = sym

        # 0, 6, 9
        for sym in sixes:
            if CommonChars(key[3], sym) == 5:
                key[9] = sym
            elif CommonChars(key[7], sym) == 3:
                key[0] = sym
            elif CommonChars(key[7], sym) == 2:
                key[6] = sym

        total += DecodeMessage(segment[1].split(), key)
    return total


# Output
print(sol5(FileReadDayTwo("Solution Three Data")))

