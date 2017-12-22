def ranges_from_set(numbers):
    numbers = sorted(numbers)
    result = []
    add_range = lambda current_range: result.append(range(current_range[0], current_range[-1] + 1))
    current_range = [numbers[0]]
    for last, current in zip(numbers, numbers[1:]):
        if current - last == 1:
            current_range.append(current)
        else:
            add_range(current_range)
            current_range = [current]
    add_range(current_range)
    return result

def range_as_list(trange):
    return [trange.start, trange.stop - 1]

def ranges_as_lists(range_list):
    return [range_as_list(r) for r in range_list]

def rangeset(*args):
    return set(range(*args))

def copy2(lst):
    return [sub.copy() for sub in lst]

def jakie(maximum, base_questions):
    opposite_operators = {"m": "wr", "w": "mr", "r": "n"}
    base_possible = set(range(1, maximum + 1))
    all_possible = set()
    for lie in range(len(base_questions) + 1):
        possible = base_possible.copy()
        questions = copy2(base_questions)
        if lie != len(base_questions):
            lied = questions[lie]; lied[1] = opposite_operators[lied[1]]
        for number, operator in questions:
            if  operator == "m":
                possible -= rangeset(number, maximum + 1)
            elif operator == "mr":
                possible -= rangeset(number + 1, maximum + 1)
            elif operator == "w":
                possible -= rangeset(1, number + 1)
            elif operator == "wr":
                possible -= rangeset(1, number)
            elif operator == "r":
                possible = {number}
            elif operator == "n":
                possible.discard(number)
        all_possible |= possible
    return ranges_as_lists(ranges_from_set(all_possible))

if __name__ == "__main__":
    tests = [(10, [[5, "m"], [2, "w"], [4, "m"], [1, "w"]]),
             (10, [[5, "m"], [2, "w"], [1, "w"], [6, "r"]])]
    for test in tests:
        r = jakie(*test)
        print(r)