from copy import deepcopy

filename = './15.input'
lines = []

with open(filename) as f:
    lines = list(map(lambda x: list(map(int, list(x.strip()))), f.readlines()))


def in_range(pos, list_):
    x, y = pos
    return 0 <= x and x <= (len(list_) - 1) and 0 <= y and y <= (len(list_[0]) - 1)


def get_neighbors(list_, pos):
    x, y = pos
    possibilities = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return list(map(lambda x: list_[x[0]][x[1]], filter(lambda x:  in_range(x, list_), possibilities)))


def expand(lines, times):
    new_lines = deepcopy(lines)
    height = len(new_lines)
    width = len(new_lines[0])
    for i in range(1, times+1):
        for idx, line in enumerate(map(lambda x: x[(i-1)*width:i*width], new_lines)):
            new_lines[idx].extend(
                [(x+1) % 10 if (x+1) % 10 != 0 else 1 for x in line]
            )
    for i in range(1, times+1):
        for line in new_lines[(i-1)*height:i*height]:
            new_lines.append(
                [(x+1) % 10 if (x+1) % 10 != 0 else 1 for x in line]
            )
    return new_lines


def find_paths(lines_):
    costs = [[float('inf') for _ in lines_[0]] for _ in lines_]
    costs[0][0] = 0
    cached = None
    iters = 0
    while True:
        iters += 1
        for y in range(len(costs)):
            for x in range(len(costs[0])):
                minimum = min(get_neighbors(costs, (y, x)))
                costs[y][x] = min(minimum + lines_[y][x], costs[y][x])
        if costs == cached:
            break
        cached = deepcopy(costs)
    return costs


def step1():
    paths = find_paths(lines)
    print(paths[-1][-1])


def step2():
    new_lines = expand(lines, 4)
    paths = find_paths(new_lines)
    print(paths[-1][-1])


step1()
step2()
