def find_shortest_path(graph, start="d", end="s"):
    to_visit = [(start, 0)]
    min_cost = float("INF")
    while to_visit:
        node, current_cost = to_visit.pop(0)
        if node == end:
            min_cost = current_cost if current_cost < min_cost else min_cost
            continue
        for neighbour, cost in graph[node].items():
            to_visit.append((neighbour, current_cost + cost))
    return min_cost

def droga(signs):
    graph = {}
    nodes = set()
    for node_from, node_to, cost in signs:
        nodes |= {node_from, node_to}
        graph.setdefault(node_from, {})[node_to] = cost

    return find_shortest_path(graph)

if __name__ == "__main__":
    tests = [[["d", "p1", 10], ["d", "p2", 20], ["p1", "p3", 20], ["p2", "p3", 5], ["p2", "s", 30], ["p3", "s", 5]]]
    for test in tests:
        r = droga(test)
        print(r)