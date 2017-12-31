def droga(path):
    height = 0
    result = 0
    for item in path:
        if isinstance(item, int):
            result += height + item
            height = 0
        elif isinstance(item, list):
            result += item[0] + abs(height - item[1])
            height = item[1]
    result += height
    return result

droga([[40,20],[50,30],10,[20,20],20,[40,10]])
