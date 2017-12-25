def ilecyfr(number_o, base):
    result = []
    number = number_o
    while number:
        number, mod = divmod(number, base)
        result.append(mod)
    result.reverse()
    return len(result)

print(ilecyfr(123456, 10))
print(ilecyfr(1, 5))
print(ilecyfr(255, 2))
print(ilecyfr(255, 16))
