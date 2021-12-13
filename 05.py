def first(filename):
    data = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            line = line.split(' -> ')
            start = line[0].split(',')
            end = line[1].split(',')
            if start[0] != end[0] and start[1] != end[1]:
                continue
            if start[0] == end[0]:
                start_index = int(start[1])
                end_index = int(end[1])
                def fixed(x): return start[0] + ',' + str(x)
            else:
                start_index = int(start[0])
                end_index = int(end[0])
                def fixed(x): return str(x) + ',' + start[1]
            if start_index > end_index:
                start_index, end_index = end_index, start_index
            end_index += 1
            for i in range(start_index, end_index):
                coord = fixed(i)
                if coord not in data:
                    data[coord] = 0
                data[coord] += 1
    counter = 0
    for i in data:
        if data[i] > 1:
            counter += 1
    return counter


def second(filename):
    data = {}
    counter = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            line = line.split(' -> ')
            start = list(map(int, line[0].split(',')))
            end = list(map(int, line[1].split(',')))

            start_x = start[0]
            start_y = start[1]
            end_x = end[0]
            end_y = end[1]

            if not (
                (start_x == end_x) or
                (start_y == end_y) or
                (start_x + end_y == end_x + start_y) or
                (start_x + start_y == end_x + end_y)
            ):
                continue

            y_direction = 0
            x_direction = 0

            x = start_x
            y = start_y

            if start_x > end_x:
                x_direction = -1
            if start_y > end_y:
                y_direction = -1
            if start_x < end_x:
                x_direction = 1
            if start_y < end_y:
                y_direction = 1

            def condition(x, y): return (
                (x_direction == 1 and x <= end_x) or
                (x_direction == -1 and x >= end_x) or
                (y_direction == 1 and y <= end_y) or
                (y_direction == -1 and y >= end_y)
            )

            def next_coord(x, y): return (x + x_direction, y + y_direction)

            while condition(x, y):
                coord = str(x) + ',' + str(y)
                if coord not in data:
                    data[coord] = 0
                data[coord] += 1
                if data[coord] == 2:
                    counter += 1
                x, y = next_coord(x, y)
    return counter


filename = './05.input'
print(first(filename))
print(second(filename))
