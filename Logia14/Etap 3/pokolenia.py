class defaultdict(dict):
    def __init__(self, factory, *args, **kwargs):
        self.factory = factory
        super().__init__(*args, **kwargs)
    def __missing__(self, key):
        self[key] = self.factory()
        return self[key]

def pokolenia(pairs):
    names = set()
    parent_of = {}
    children_of = defaultdict(set)
    for parent, child in pairs:
        names.add(parent)
        names.add(child)
        parent_of[child] = parent
        children_of[parent].add(child)
    elder = next(iter(names - set(parent_of.keys())))
    depth_of = {}
    stack = [(elder, 0)]
    while stack:
        node, depth = stack[-1]
        depth_of[node] = depth
        stack.pop()
        for child in children_of[node]:
            stack.append((child, depth + 1))
    nodes_by_depth = defaultdict(set)
    for key, value in depth_of.items():
        nodes_by_depth[value].add(key)
    result = []
    for key, value in sorted(nodes_by_depth.items()):
        if key == 0:
            result.append(next(iter(value)))
        else:
            result.append(sorted(value))
    return result

if __name__ == "__main__":
    print(pokolenia([["a", "b"], ["b", "x"], ["a", "d"], ["a", "z"]]))
    print(pokolenia([["Ula", "Ala"], ["Ola", "Ula"], ["Ela", "Ola"], ["Ela", "Jan"]]))
