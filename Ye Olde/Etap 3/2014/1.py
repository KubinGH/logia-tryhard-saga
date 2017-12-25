def dict_levels(dictionary, start, reverse_result=True):
    result = {}
    checked = [start]
    to_check = [(0, start)]
    while to_check:
        c_level, current = to_check.pop(0)
        if not reverse_result:
            result[current] = c_level
        else:
            result.setdefault(c_level, []).append(current)
        if current in dictionary:
            for value in dictionary[current]:
                if value not in checked:
                    checked.append(value)
                    to_check.append((c_level + 1, value))
    return result

def pokolenia(pairs):
    names = set()
    children_of = {}
    parent_of = {}
    for first, second in pairs:
        names.add(first); names.add(second)
        children_of.setdefault(first, []).append(second)
        parent_of[second] = first

    head = None
    for name in names:
        parent = parent_of.setdefault(name, None)
        if parent is None:
            if head is None:
                head = name
            else:
                raise ValueError("Multiple heads of family")
    if head is None:
        raise ValueError("Missing head of family")  

    generations = dict_levels(children_of, head, reverse_result=True)

    result = []
    for generation, lst in sorted(generations.items()):
        if generation == 0:
            result.append(lst[0])
        else:
            result.append(lst)

    return result
    
