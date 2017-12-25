def fixed_bin(value, length=None):
    result = bin(value)[2:]
    if length is not None: result = result.zfill(length)
    return result

def abc(word, key, n):
    n -= 1
    combinations = set()

    for i in range(2**len(word)):
        ibin = fixed_bin(i, len(word))
        icom = "".join([word[j] for j, bin_value in enumerate(ibin) if bin_value == "1"])
        idx = 0
        for char in icom:
            if char == key[idx]: idx += 1
            if idx == len(key): break
        else:
            continue
        combinations.add(icom)
        
    combinations = sorted(combinations)
    print(combinations)
    print("\n".join(c for c in combinations))
    
    return combinations[n] if n < len(combinations) else ""



if __name__ == "__main__":
    print("===\nTest 1\n===")
    r1 = abc("abebc", "abc", 5)
    print("===\nTest 2\n===")
    r2 = abc("xabacxy", "abc", 3)
