folds = []
dots = []

with open('./13.input') as f:
    instructions = False
    for line in f:
        line = line.strip()
        if line == '':
            instructions = True
            continue
        if not instructions:
            coords = line.split(',')
            dots.append((int(coords[0]), int(coords[1])))
            continue
        string = line.split(' ')[-1]
        folds.append(string)


def step1():
    cpy = []
    instruction = folds[0]
    coord = int(instruction.split('=')[1])
    is_y = instruction.startswith('y')
    for pair in dots:
        x, y = pair
        if is_y:  # y
            if y > coord:
                cpy.append((x, coord - (y - coord)))
            elif y < coord:
                cpy.append((x, y))
        else:  # x
            if x > coord:
                cpy.append((coord - (x - coord), y))
            elif x < coord:
                cpy.append((x, y))
    print(len(list(set(cpy))))


def step2():
    cpy = [*dots]
    i = 0
    while len(folds) > 0:
        i += 1
        instruction = folds.pop(0)
        coord = int(instruction.split('=')[1])
        is_y = instruction.startswith('y')
        new_el = []
        for pair in cpy:
            x, y = pair
            if is_y:  # y
                if y > coord:
                    new_el.append((x, coord - (y - coord)))
                elif y < coord:
                    new_el.append((x, y))
            else:  # x
                if x > coord:
                    new_el.append((coord - (x - coord), y))
                elif x < coord:
                    new_el.append((x, y))
        cpy = list(set(new_el))
    max_x = max(x for x, y in cpy)
    max_y = max(y for x, y in cpy)
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in cpy:
                print('█', end='')
            else:
                print(' ', end='')
        print()
    print()


step1()
step2()
