csum = sum

def sum(numbers):
    result = 1
    for number in numbers:
        if number <= result:
            result += number
    return result

if __name__ == "__main__":
    tests = [[1, 2, 3, 4, 100],
             [1, 1, 2, 3, 5, 18, 21]]

    for test in tests:
        r = sum(test)
        print(r)