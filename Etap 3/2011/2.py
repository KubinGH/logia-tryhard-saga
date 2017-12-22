#itertools.zip_longest
def zip_longest(iterables, fillvalue=None):
    sentinel = object()
    iterators = [iter(iterable) for iterable in iterables]
    exhausted = [False for _ in range(len(iterators))]
    while not all(exhausted):
        #print("iter")
        #print("e", exhausted)
        current = [fillvalue if empty else sentinel for empty in exhausted]
        #print("c", current)
        for i, item in enumerate(current):
            if item == fillvalue:
                continue
            try:
                current[i] = next(iterators[i])
            except StopIteration:
                exhausted[i] = True
                current[i] = fillvalue
        if not all(item == fillvalue for item in current):
            yield current
        else:
            break

def sum_digits(string):
    return sum(int(digit) for digit in string)

def kostka(gamelog):
    gamelog = [[pair[0], str(pair[1])] for pair in gamelog]
    names = [pair[0] for pair in gamelog]
    roll_list = [pair[1] for pair in gamelog]

    print(names)
    print(roll_list)

    filled_rolls = list(zip_longest(roll_list, None))
    for crolls in filled_rolls:
        print(crolls)
    last_players = [names[i] for i, roll in enumerate(filled_rolls[-1]) if roll == "6"]
    print(last_players)
    if len(last_players) == 1: return last_players[0]
    sums = {name: sum_digits(roll_list[i]) for i, name in enumerate(last_players)}
    print(sums)
    return max(names, key=lambda name: sums[name] if name in sums else -1)

if __name__ == "__main__":
    tests = [ [["Danka",  555], ["Andrzej", 236116], ["Marek", 326336616], ["Adam", 416516636], 
               ["Karol", 416126], ["Grzesio", 1461564], ["Krzysio", 342]]]

    for test in tests:
        r = kostka(test)
        print(r)