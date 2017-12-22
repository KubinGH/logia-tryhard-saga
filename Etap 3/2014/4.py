class TruckTooFull(Exception): pass

class Truck:
    def __init__(self, max_weight):
        self.weight_in = 0
        self.max_weight = max_weight

    def load(self, weight):
        if self.can_load(weight):
            self.weight_in += weight
        else:
            raise TruckTooFull

    def can_load(self, weight):
        return (self.weight_in + weight) <= self.max_weight
    
def ilesam(package_series, truck_data):
    packages = [weight for quantity, weight in package_series
                       for _ in range(quantity)]
    trucks = [Truck(max_weight) for max_weight in truck_data]

    result = 0
    while packages:
        current = packages[0]
        current_truck = trucks[0]
        try:
            current_truck.load(current)
        except TruckTooFull:
            trucks.pop(0)
            result += 1
        else:
            packages.pop(0)
    if trucks[0].weight_in != 0:
        result += 1
    
    return result  
