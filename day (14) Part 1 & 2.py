def ReadFile (name):
    dict = {}
    with open(name, 'r') as data:
        sentence = None
        for line in data.readlines():
            if sentence is None:
                sentence = line.split()[0]
            elif len(line.split()) > 1:  # Removes line = " "
                l = line.split()
                dict[l[0]] = l[2]
    return sentence, dict

# Functions that subtracts the most common letter (by length) by the least common letter (by length)
def difference_max_min (word, letters):
    let = {}
    max_let, min_let = letters[0], letters[0]
    for letter in letters:
        let[letter] = len([x for x in word if x == letter])
        if let[max_let] < let[letter]:
            max_let = letter
        elif let[min_let] > let[letter]:
            min_let = letter
    return let[max_let] - let[min_let]



# Day 14 Problem One
def DayOne (prompt, ref):
    for _ in range(10):
        string = f"{prompt[0]}"
        for i in range(1, len(prompt)):
            j = i - 1
            string += ref[prompt[j] + prompt[i]] + prompt[i]
        prompt = string
    letters = tuple(set([x for x in prompt]))
    return difference_max_min(prompt, letters)

# Day 14 Problem Two
def DayTwo (word, ref):
    pairs = {}
    end_pair = ""
    for i in range(1, len(word)):
        j = i - 1
        if word[j] + word[i] not in pairs:
           pairs[word[j] + word[i]] = 1
        elif word[j] + word[i] in pairs:
            pairs[word[j] + word[i]] += 1

    for step in range(40):
        temp = {}
        count = 0
        for i, j in pairs.items():
            count += 1
            # End Pair Condition
            if step == 39 and count == len(pairs):
                end_pair = i
            else:
                let = ref[i]
                one, two = i[0], i[1]
                # Pair One
                if one + let not in temp.keys():
                    temp[one + let] = j
                elif one + let in temp.keys():
                    temp[one + let] += j
                # Pair Two
                if let + two not in temp.keys():
                    temp[let + two] = j
                elif let + two in temp.keys():
                    temp[let + two] += j
        pairs = temp

    # Count of Letters
    letters = {}
    for i, j in pairs.items():
        # Only Counts the First letter of each pair
        name = i[0]
        if name not in letters.keys():
            letters[name] = j
        elif name in letters.keys():
            letters[name] += j
    # Then Counts all the letters in the end pair
    if end_pair[0] not in letters.keys():
        letters[end_pair[0]] = 1
    elif end_pair[0] in letters.keys():
        letters[end_pair[0]] += 1
    if end_pair[1] not in letters.keys():
        letters[end_pair[1]] = 1
    elif end_pair[1] in letters.keys():
        letters[end_pair[1]] += 1

    vals = letters.values()
    return max(vals) - min(vals)
