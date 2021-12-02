count = -1
prev = 0
lines = []
with open("01.input") as f:
    for i, line in enumerate(f):
        lines.append(line)

for i, line in enumerate(lines):
    num = int(line)
    if num > prev:
      count += 1
    prev = num

print(count)