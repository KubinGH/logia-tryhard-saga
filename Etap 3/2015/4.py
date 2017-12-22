class Building:
    def __init__(self, width, height):
        self.width, self.height = width, height

class Lizard:
    def __init__(self):
        self.x = self.y = 0
        self.walked = 0

    def cross(self, building):
        if building.height != self.y:
            self.walked += abs(building.height - self.y)
            self.y = building.height
        self.walked += abs(building.width)
        self.x += building.width

    def go_to_floor(self):
        self.walked += abs(self.y)
        self.y = 0        

def is_seq(obj):
    return isinstance(obj, (list, tuple))

def droga(buildings):
    buildings = [Building(*item) if is_seq(item) else Building(item, 0)
                 for item in buildings]

    tom = Lizard()
    for building in buildings:
        tom.cross(building)
    tom.go_to_floor()

    return tom.walked
