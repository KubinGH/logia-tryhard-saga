def sum_last_digit(a, b):
    return int(str(a + b)[-1])


class Table:
    ROTATIONS = ["p", "g", "l", "d"]
    DEFAULT_ROT = ROTATIONS[0]
    def __init__(self, data):
        assert all(len(data[0]) == len(row) for row in data), \
               "Data needs to have rows of equal size"
        self.data = data
        self.rot = 0

    @property
    def width(self):
        return len(self.data[0])

    @property
    def height(self):
        return len(self.data)

    @property
    def rotation_str(self):
        return self.ROTATIONS[self.rot]

    def pprint(self):
        print("Table {")
        for row in self.data:
            print(row)
        print("}")

    def rotate_once(self):
        self.rot += 1
        self.rot %= 4
        self.data = [list(row) for row in zip(*self.data[::-1])]

    def rotate_till(self, direction_str):
        while self.rotation_str != direction_str:
            self.rotate_once()

    def reset_rotation(self):
        self.rotate_till(self.DEFAULT_ROT)
            
    def push_numbers(self, direction=DEFAULT_ROT):
        self.rotate_till(direction)

        d = self.data
        changes = True
        while changes:
            changes = False
            for y, row in enumerate(self.data):
                for i in range(len(row) - 1):
                    if row[i] == 0: continue
                    if row[i] == row[i + 1]:
                        changes = True
                        last_digit = sum_last_digit(row[i], row[i + 1])
                        row[i], row[i + 1] = 0, last_digit
                    elif row[i + 1] == 0:
                        changes = True
                        row[i], row[i + 1] = 0, row[i]
        
        self.reset_rotation()
 

def redukcja(raw_table, directions):
    table = Table(raw_table)
    for direction in directions:
        table.push_numbers(direction)
    table.reset_rotation()
    return table.data
    
