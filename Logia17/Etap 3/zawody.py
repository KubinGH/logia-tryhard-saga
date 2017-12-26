from string import ascii_uppercase
def zawody(rounds):
    players = list(ch for ch in ascii_uppercase[:len(rounds[0])])
    for points in rounds:
        players.pop(points.index(min(points)))
    return players[0]

print(zawody([[8,9]]))
print(zawody([[4,0,2,1],[1,2,3],[2,1]]))
