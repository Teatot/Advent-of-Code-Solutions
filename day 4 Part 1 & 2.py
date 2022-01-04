def ReadFile (name):
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


# Marks the called number on the board
def Mark (board, num):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == num:
                board[r][c] = "X"
    return board

# Checks if there is a bingo
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

# Calculates the sum of the unmarked numbers on the board
def CalculateSum (board):
    sum = 0
    for row in board:
        for num in row:
            if type(num) is int:
                sum += num
    return sum


# Day 4 Problem One
def DayOne (nums, boards):
    for num in nums:
        for board in boards:
            board = Mark(board, num)
            if Bingo(board):
                return CalculateSum(board) * num

# Day 4 Problem Two
def DayTwo (nums, boards):
    solved = 0
    solved_b = []
    for num in nums:
        for ind in range(len(boards)):
            if ind not in solved_b:
                boards[ind] = Mark(boards[ind], num)
                if Bingo(boards[ind]):
                    if solved == len(boards) - 1:
                        return CalculateSum(boards[ind]) * num
                    else:
                        solved += 1
                        solved_b.append(ind)
