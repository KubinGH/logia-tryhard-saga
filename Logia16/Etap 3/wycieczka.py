from collections import defaultdict
def opis(first_visit, second_or_none):
    if not first_visit or not second_or_none:
        return []
    index = 0
    current_city = first_visit[0]
    visited = {current_city}
    graph = defaultdict(list)
    for city in first_visit[1:]:
        graph[current_city].append(city)
        visited.add(current_city); visited.add(city)
        if city != second_or_none[index]:
            current_city = city
        else:
            for second_city in second_or_none[index+1:]:
                index += 1
                if second_city in visited:
                    current_city = second_city
                else:
                    break

    root = first_visit[0]
    def traveller(current=root, graph=graph):
        diary = []
        diary.append(current)
        if graph[current]:
            for neighbour in graph[current]:
                diary.extend(traveller(neighbour))
                diary.append(current)
        return diary

    full_diary = traveller()
    last_visit = []
    for city in full_diary[::-1]:
        if len(last_visit) == len(visited):
            break
        else:
            if city not in last_visit:
                last_visit.insert(0, city)

    return last_visit
    
