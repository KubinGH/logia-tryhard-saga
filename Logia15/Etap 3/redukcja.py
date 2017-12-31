rotations = {
    "p": 0,
    "g": 1,
    "l": 2,
    "d": 3
}

def move_to_right(array):
    for row in array:
        changes = True
        while changes:
            changes = False
            for i in range(len(row) - 1):
                if row[i] == row[i + 1] != 0:
                    row[i], row[i + 1] = 0, (row[i] + row[i + 1]) % 10
                    changes = True
                elif row[i] and not row[i + 1]:
                    row[i], row[i + 1] = 0, row[i]
                    changes = True

def rotated(array):
    return [list(row) for row in zip(*array[::-1])]

def redukcja(array, moves):
    for move in moves:
        for _ in range(rotations[move]):
            array = rotated(array)
        move_to_right(array)
        for _ in range((4 - rotations[move]) % 4):
            array = rotated(array)
    return array
