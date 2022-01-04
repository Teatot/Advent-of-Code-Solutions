def ReadFile(name):
    segments = []
    with open(name, 'r') as data:
        codes = data.read().split("\n")
        for c in codes:
            segments.append(c.split("|"))
    return segments


# Returns how many letters are common between a, b
def CommonChars (a, b):
    common = 0
    for i in a:
        for j in b:
            if i == j:
                common += 1
    return common

# Decodes the message, with the reference, as returns its numerical value
def DecodeMessage (message, ref):
    line = ""
    for code in message:
        for i in range(10):
            if sorted(code) == sorted(ref[i]):
                line += str(i)
                break
    return int(line)


# Day 8 Problem One
def DayOne (codes):
    total = 0
    for segment in codes:
        for code in segment[1].split():
            if len(code) in (2, 3, 4, 7):
                total += 1
    return total

# Day 8 Problem Two
def DayTwo (codes):
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
