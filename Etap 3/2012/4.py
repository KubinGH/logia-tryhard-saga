def get_cost(graph, city1, city2):
    neighbours = graph[city1]
    return neighbours[city2]

def euro(team_data, matches, connections):
    teams = set()
    team_base = {}
    for name, base in team_data:
        team_base[name] = base
        teams.add(name)

    cities = set()
    graph = {}
    for city1, city2, cost in connections:
        graph.setdefault(city1, {})[city2] = cost
        graph.setdefault(city2, {})[city1] = cost
        cities.add(city1); cities.add(city2)

    for city in cities:
        graph[city][city] = 0

    team_travel_time = {name: 0 for name in teams}
    for team1, team2, city in matches:
        cost1 = get_cost(graph, team_base[team1], city)
        cost2 = get_cost(graph, team_base[team2], city)
        team_travel_time[team1] += cost1
        team_travel_time[team2] += cost2

    return min(team_travel_time, key=lambda x: team_travel_time[x])

if __name__ == "__main__":
    tests = [([["A", "M1"], ["B", "M2"], ["C", "M1"], ["D", "M3"]], 
              [["A", "B", "M1"], ["A", "C", "M1"], ["A", "D", "M3"], ["B", "C", "M1"], ["B", "D", "M3"], ["C", "D", "M3"]], 
              [["M1", "M2", 1], ["M1", "M3", 5], ["M2", "M3", 6]]),

            ([["D1", "M1"], ["D2", "M2"], ["D3", "M3"], ["D4", "M4"]],
             [["D1", "D3", "M5"], ["D2", "D4", "M6"], ["D1", "D2", "M5"], ["D3", "D4", "M6"], ["D1", "D4", "M5"], ["D2", "D3", "M6"]],
             [["M1", "M5", 20], ["M1", "M6", 5], ["M2", "M5", 15], ["M2", "M6", 10], ["M3", "M5", 25], ["M3", "M6", 20], ["M4", "M5", 20], ["M4", "M6", 20]])
    ]

    for test in tests:
        r = euro(*test)
        print(r)
