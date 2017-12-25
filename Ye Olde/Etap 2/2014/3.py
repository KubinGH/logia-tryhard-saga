def kosp(raw_one, raw_two):
    if not raw_one or not raw_two: return 0
    
    start_one = raw_one[0]
    start_two = raw_two[0]
    path_one = [raw_one[0]]
    path_two = [raw_two[0]]
    one = {start_one: 0}
    two = {start_two: 0}
    
    iter_one = (raw_one, one, path_one, start_one)
    iter_two = (raw_two, two, path_two, start_two)
    for craw, cdict, cpath, cstart in (iter_one, iter_two):
        value = None; last_key = cstart
        for ch in craw[1:]:
            if value is None:
                value = int(ch)
            else:
                cpath.append(ch)
                cdict[ch] = value + cdict[last_key]
                value = None; last_key = ch
        cdict["center"] = value + cdict[last_key]
        cpath.append("center")

    last_common = None
    for station_one, station_two in zip(reversed(path_one), reversed(path_two)):
        if station_one == station_two:
            last_common = station_one
        else:
            break

    return one[last_common] + two[last_common]
    
