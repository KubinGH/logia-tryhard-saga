def shift(lst, n=1):
    for _ in range(n):
        lst.append(lst.pop(0))

def ostatni(people_n, every):
    gone = 0
    people_lst = [i + 1 for i in range(people_n)]
    while len(people_lst) > 1:
        shift(people_lst, every - 1)
        people_lst.pop(0)
    return people_lst[0]

if __name__ == "__main__":
    print(ostatni(7, 3))
    print(ostatni(6, 2))
