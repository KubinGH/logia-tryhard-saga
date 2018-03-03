def ilesam(packs, cars):
    pack_idx, product = 0, 0
    for c, weight in enumerate(cars):
        while pack_idx < len(packs) and weight >= packs[pack_idx][1]:
            taken = weight // packs[pack_idx][1]
            if taken >= packs[pack_idx][0] - product:
                weight -= (packs[pack_idx][0] - product) * packs[pack_idx][1]
                pack_idx += 1
                product = 0
            else:
                product += taken
                weight -= taken * packs[pack_idx][1] 
        if pack_idx == len(packs):
            break
    return c + 1

if __name__ == '__main__':
    print(ilesam([[4, 5], [2, 2], [1, 20]], [17, 25, 25, 17, 25]))
    print(ilesam([[20, 1], [2, 5], [1, 3], [2, 7]], [25, 10, 10, 10, 10, 10]))
