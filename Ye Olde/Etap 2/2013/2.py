def highest_true(iterable, function):
    sentinel = object()
    last_true = sentinel
    for item in iterable:
        if function(item):
            last_true = item
        else:
            if last_true is not sentinel:
                return last_true
            else:
                raise ValueError("No value evaluated to True")
    else:
        raise ValueError("Every value evaluated to True")

def kiedy(climb, fall, shelves_interval):
    pole_height = 1000

    if shelves_interval == 0:
        shelves = []
    else:
        shelves = [sh for sh in range(0, pole_height + 1, shelves_interval)]        

    height = 0
    day = 0
    while True:
        day += 1
        height += climb
        if height >= pole_height: return day
        if shelves:
            shelve = highest_true(shelves, lambda x: x <= height)
        else:
            shelve = 0
        height = max(height - fall, shelve)
        
