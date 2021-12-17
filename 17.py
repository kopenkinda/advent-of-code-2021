x = [0, 0]
y = [0, 0]

with open('./17.input') as f:
    line = f.readline().strip()
    line = line.split(' ')
    line = list(map(lambda x: x.split('..'), line[-2:]))
    x[0] = int(line[0][0][2:])
    x[1] = int(line[0][1][:-1])
    y[0] = int(line[1][0][2:])
    y[1] = int(line[1][1])


def is_in_range(x, y, x_range, y_range):
    return x_range[0] <= x and x <= x_range[1] and y_range[0] <= y and y <= y_range[1]


def passed_range(x, y, x_vel, x_range, y_range):
    if y < min(y_range[1], y_range[0]):
        return True
    if x_vel > 0 and x > x_range[1]:
        return True
    if x_vel < 0 and x < x_range[0]:
        return True
    return False


def simulate(x_vel, y_vel, x_range, y_range):
    x = 0
    y = 0
    while not passed_range(x, y, x_vel, x_range, y_range):
        x += x_vel
        y += y_vel
        x_vel = x_vel - 1 if x_vel > 0 else x_vel + 1 if x_vel < 0 else 0
        y_vel -= 1
        if is_in_range(x, y, x_range, y_range):
            return True
    return False


def find_passing_through(x_range, y_range):
    pts = []
    iters = abs(min(y_range[0], y_range[1])) * 2 + 1
    for i in range(iters * -1, iters + 1):
        for j in range(iters * -1, iters + 1):
            if simulate(i, j, x_range, y_range):
                pts.append((i, j))
    return pts


def find_highest_y(points):
    mapped = []
    for point in points:
        x = 0
        y = 0
        x_vel = point[0]
        y_vel = point[1]
        while True:
            x += x_vel
            if y > y + y_vel:
                mapped.append(y)
                break
            y += y_vel
            x_vel = x_vel - 1 if x_vel > 0 else x_vel + 1 if x_vel < 0 else 0
            y_vel -= 1
    return max(mapped)


pts = find_passing_through(x, y)


def step1():
    print(find_highest_y(pts))


def step2():
    print(len(pts))


step1()
step2()
