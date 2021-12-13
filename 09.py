data = []

with open('./09.input') as f:
    for line in f:
        data.append(list(map(int, line.strip())))


def calc_lows():
    lows = []
    for y, row in enumerate(data):
        for x, el in enumerate(row):
            top = True
            left = True
            right = True
            bottom = True
            try:
                if el >= data[y][x-1]:
                    left = False
            except IndexError:
                pass
            try:
                if el >= data[y][x+1]:
                    right = False
            except IndexError:
                pass
            try:
                if el >= data[y-1][x]:
                    top = False
            except IndexError:
                pass
            try:
                if el >= data[y+1][x]:
                    bottom = False
            except IndexError:
                pass
            if top and left and right and bottom:
                lows.append((y, x))
    return lows


def calc_basins(pair):
    basin_parts = [pair]
    y, x = pair
    current_num = data[y][x]
    try:
        left_num = data[y][x-1]
        if left_num > current_num and left_num < 9:
            basin_parts.extend(calc_basins((y, x-1)))
    except IndexError:
        pass
    try:
        right_num = data[y][x+1]
        if right_num > current_num and right_num < 9:
            basin_parts.extend(calc_basins((y, x+1)))
    except IndexError:
        pass
    try:
        top_num = data[y-1][x]
        if top_num > current_num and top_num < 9:
            basin_parts.extend(calc_basins((y-1, x)))
    except IndexError:
        pass
    try:
        bottom_num = data[y+1][x]
        if bottom_num > current_num and bottom_num < 9:
            basin_parts.extend(calc_basins((y+1, x)))
    except IndexError:
        pass

    distinct = list(set(basin_parts))

    for i in range(len(distinct)):
        if distinct[i][0] < 0 or distinct[i][1] < 0:
            distinct.pop(i)
    return distinct


def step1():
    lows = calc_lows()
    counter = 0
    for pair in lows:
        y, x = pair
        counter += data[y][x] + 1
    print(counter)


def step2():
    basins = []
    lows = calc_lows()
    for pair in lows:
        basins.append(calc_basins(pair))

    basins = sorted(list(map(lambda x: len(x), basins)))
    three_highest = basins[-3:]
    counter = 1
    print(three_highest)
    for i in three_highest:
        counter *= i
    print(counter)


step1()
step2()
