hor = 0
depth = 0

with open('./02.input') as f:
    for line in f:
        line = line.strip()
        if line:
            split = line.split(' ')
            instruction = split[0]
            num = int(split[1])
            if instruction == 'up':
                depth -= num
            elif instruction == 'down':
                depth += num
            elif instruction == 'forward':
                hor += num

print(hor*depth)

hor = 0
depth = 0
aim = 0

with open('./02.input') as f:
    for line in f:
        line = line.strip()
        if line:
            split = line.split(' ')
            instruction = split[0]
            num = int(split[1])
            if instruction == 'up':
                aim -= num
            elif instruction == 'down':
                aim += num
            elif instruction == 'forward':
                hor += num
                depth += aim * num

print(hor*depth)
