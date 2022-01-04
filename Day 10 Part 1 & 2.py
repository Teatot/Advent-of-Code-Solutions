from math import *


def ReadFile (name):
    lines = []
    with open(name, 'r') as data:
        for lin in data.readlines():
            lines.append([x for x in lin if x != '\n'])
    return lines

# Adds Front to the Queue, Checks Backs to the last element in the queue
# If match, the last element is removed
def Check_End (sym, q):
    braces = {")":"(", "]":"[", "}":"{", ">":"<"}

    if sym in ("(", "[", "{", "<"):
        q.append(sym)
        return

    if q[-1] == braces[sym]:
        q.pop()
        return

    q.append(sym)

# Checks if all the items in the array are all fronts
def is_valid (arr):
    lst = []
    for it in arr:
        if it in ("(", "[", "{", "<"):
            lst.append(True)
        else:
            lst.append(False)
    return True if len(set(lst)) == 1 else False


# Day Ten Problem One
def DayOne (lines):
    wrg_end = 0
    points = {")":3, "]":57, "}":1197, ">":25137}
    for code in lines:
        lst = []
        for sym in code:
            Check_End (sym, lst)
        for it in lst:
            if it in (")", "]", "}", ">"):
                wrg_end += points[it]
                break
    return wrg_end

# Day Ten Problem Two
def DayTwo (lines):
    nums = []
    points = {"(":1, "[":2, "{":3, "<":4}
    for code in lines:
        lst = []
        for sym in code:
            Check_End(sym, lst)
        if is_valid(lst):
            score = 0
            for it in lst[::-1]:
                score *= 5
                score += points[it]
            nums.append(score)
    nums = sorted(nums)
    mid = ceil(len(nums)/2) - 1
    return nums[mid]
