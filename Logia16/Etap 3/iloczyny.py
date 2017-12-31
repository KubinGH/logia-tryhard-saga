import math

def liczby(numbers):
    result = []
    for n in numbers:
        try:
            d = max(i for i in range(2, math.ceil(math.sqrt(n)) + 1) if not n % i)
        except ValueError:
            d = 1
        result.append([d, n // d])
    return result
