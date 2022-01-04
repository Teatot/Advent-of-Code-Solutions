def ReadFile (name):
    with open(name, 'r') as data:
        l = ""
        for line in data.readlines():
            l += str(line)
    return l.split("\n")


# Either returns the most frequent or least frequent number (0 or 1)
# Returns -1 if they're equivalent
def Freq (list, place, key="most"):
    on, off = 0,0
    for bin in list:
        if bin[place] == '1':
            on += 1
        else:
            off += 1
    if (on > off and key == "most") or (off > on and key == "least"):
        return '1'
    elif (off > on and key == "most") or (on > off and key == "least"):
        return '0'
    else:
        return '-1'


# Day 3 Problem One
def DayOne (list):
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
def DayTwo (list):
    o, c = list, list
    for i in range(len(list[0])):
        if len(o) > 1:
            pop_o = Freq(o, i)
            if pop_o == '0':
                o = [x for x in o if x[i] == "0"]
            elif pop_o == '1' or pop_o == '-1':
                o = [x for x in o if x[i] == "1"]
        if len(c) > 1:
            pop_c = Freq(c, i, key="least")
            if pop_c == '1':
                c = [x for x in c if x[i] == '1']
            elif pop_c == '0' or pop_c == '-1':
                c = [x for x in c if x[i] == "0"]
    return int(o[0], 2) * int(c[0], 2)
