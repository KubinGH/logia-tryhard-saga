def litera(strings):
    counter = {}
    for string in strings:
        for char in string:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
    most_common = []
    most_common_count = 0
    for key, value in counter.items():
        if value > most_common_count:
            most_common = [key]
            most_common_count = value
        elif value == most_common_count:
            most_common.append(key)
    return most_common if len(most_common) > 1 else most_common[0]
