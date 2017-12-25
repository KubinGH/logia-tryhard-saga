def cycle_nelems(items, count):
    result = []
    count = list(count)
    current = 0
    while any(count):
        if count[current]:
            result.append(items[current])
            count[current] -= 1
        current = (current + 1) % len(items)
    return result


def non_matching_idx(first_arr, second_arr):
    result = []
    for i, items in enumerate(zip(first_arr, second_arr)):
        if items[0] != items[1]: result.append(i)
    return result

def kulki(arrangement):
    red, green = "c", "z"
    start_arr = [ch for ch in arrangement]
    arr_len = len(start_arr)

    count = {}
    count[red] = start_arr.count(red)
    count[green] = arr_len - count[red]

    final_arr = cycle_nelems((red, green), (count[red], count[green]))
    to_replace = non_matching_idx(start_arr, final_arr)

    return len(to_replace) // 2

if __name__ == "__main__":
    tests = ["czczczzz",
             "czczzczz",
             "zczc"]

    for test in tests:
        print(kulki(test))
