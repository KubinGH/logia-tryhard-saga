def poler(path):
    dirs = {"g": [0, 1], "d": [0, -1],
            "p": [1, 0], "l": [-1, 0]}

    pos = [0, 0]
    max_pos = {k: 0 for k in "gdpl"}

    for cdir in path:
        pos = [p + d for p, d in zip(pos, dirs[cdir])]
        max_pos["g"] = max(max_pos["g"], pos[1])
        max_pos["d"] = min(max_pos["d"], pos[1])
        max_pos["p"] = max(max_pos["p"], pos[0])
        max_pos["l"] = min(max_pos["l"], pos[0])

    return (max_pos["g"] - max_pos["d"]) * (max_pos["p"] - max_pos["l"])

