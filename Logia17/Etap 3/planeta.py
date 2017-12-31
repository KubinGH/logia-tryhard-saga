class DisjointSetTree:
    def __init__(self, init_nodes=()):
        self.rank = {}
        self.parent = {}
        for node in init_nodes:
            self.init_node(node)

    def init_node(self, node):
        self.rank[node] = 0
        self.parent[node] = node

    def find_root(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.find_root(self.parent[node])
            return self.parent[node]

    def merge(self, first_node, second_node):
        first, second = self.find_root(first_node), self.find_root(second_node)
        if self.rank[second] > self.rank[first]:
            self.rank[second] += 1
            self.parent[first] = second
        else:
            self.rank[first] += 1
            self.parent[second] = first

def distance(first, second, size):
    a1, a2, b1, b2 = *first, *second
    if b1 < a1: a1, b1 = b1, a1
    if b2 < a2: a2, b2 = b2, a2
    v11, v12 = b1 - a1, a1 + size - b1
    v21, v22 = b2 - a2, a2 + size - b2
    return min(v11, v12) + min(v21, v22)

def planeta(size, houses):
    houses = [tuple(house) for house in houses]
    tree = DisjointSetTree(houses)
    for house_from in houses:
        for house_to in houses:
            if distance(house_from, house_to, size) <= 5:
                tree.merge(house_from, house_to)
    counter = {}
    for house in houses:
        root = tree.find_root(house)
        if root not in counter:
            counter[root] = 0
        counter[root] += 1
    return max(counter.values())

print(planeta(12,[[3,1],[1,1],[1,3],[2,12],[9,5],[8,6]]))
print(planeta(100,[[6,6],[6,11],[11,6],[11,11],[80,80]]))
print(planeta(30,[[6,6],[6,7],[6,8],[6,9],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[15,10],[16,6],[16,7],[16,8],[16,9],[16,10],[16,11],[16,12],[16,13],[16,14],[16,15],[25,25],[26,26]]))
print(planeta(50,[[6,6],[6,7],[6,8],[6,9],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[15,10],[16,7],[16,8],[16,9],[16,10],[16,11],[16,12],[16,13],[16,14],[16,15],[7,6],[8,6],[9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[15,6],[16,6],[17,10],[18,10],[19,10],[20,10],[21,10],[22,10],[23,10],[24,10],[25,10],[26,7],[26,8],[26,9],[26,10],[26,11],[26,12],[26,13],[26,14],[26,15],[17,6],[18,6],[19,6],[20,6],[21,6],[22,6],[23,6],[24,6],[25,6],[26,6],[30,28],[30,29],[30,30]]))
