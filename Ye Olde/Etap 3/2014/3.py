#itertools.cycle
def cycle(iterable):
    while True:
        for item in iterable:
            yield item

def zip_sum(first, second):
    return (e1 + e2 for e1, e2 in zip(first, second))

def spotkanie(first_dirs, second_dirs):
    dirs = {"g": (0, 1),
            "d": (0, -1),
            "p": (1, 0),
            "l": (-1, 0)}            
    
    first_dirs = cycle(first_dirs)
    second_dirs = cycle(second_dirs)

    first_pos = (0, 0)
    second_pos = (0, 0)

    for i in range(100):
        first_dir =  next(first_dirs)
        second_dir = next(second_dirs)

        first_pos  = tuple(zip_sum(first_pos,  dirs[first_dir]))
        second_pos = tuple(zip_sum(second_pos, dirs[second_dir]))

        if first_pos == second_pos:
            return i + 1


    return 0
