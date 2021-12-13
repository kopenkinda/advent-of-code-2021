grid_1 = []
grid_2 = []
empty = []

filename = '11.input'

with open(filename) as f:
  for line in f:
    nums = list(map(int, list(line.strip())))
    grid_1.append([*nums])
    grid_2.append([*nums])
    empty.append([0 for _ in nums])

def inc_grid_el(grid, light_grid, rowIdx, colIdx):
  try:
    if not light_grid[rowIdx][colIdx]:
      grid[rowIdx][colIdx] += 1
  except IndexError:
    pass

def advance_a_step(grid):
  flashes = 0
  for rowIdx in range(len(grid)):
    for colIdx in range(len(grid[rowIdx])):
      grid[rowIdx][colIdx] += 1

  flashed = []
  for rowIdx in range(len(grid)):
    flashed.append([])
    for colIdx in range(len(grid[rowIdx])):
      flashed[rowIdx].append(False)

  do_again = True
  while do_again:
    do_again = False
    for rowIdx in range(len(grid)):
      for colIdx in range(len(grid[rowIdx])):
        if grid[rowIdx][colIdx] > 9:
          grid[rowIdx][colIdx] = 0
          do_again = True
          flashes += 1
          flashed[rowIdx][colIdx] = True
          if rowIdx > 0 and not flashed[rowIdx-1][colIdx]:
            grid[rowIdx-1][colIdx] += 1
          if rowIdx < len(grid)-1 and not flashed[rowIdx+1][colIdx]:
            grid[rowIdx+1][colIdx] += 1
          if colIdx > 0 and not flashed[rowIdx][colIdx-1]:
            grid[rowIdx][colIdx-1] += 1
          if colIdx < len(grid[rowIdx])-1 and not flashed[rowIdx][colIdx+1]:
            grid[rowIdx][colIdx+1] += 1
          if rowIdx > 0 and colIdx > 0 and not flashed[rowIdx-1][colIdx-1]:
            grid[rowIdx-1][colIdx-1] += 1
          if rowIdx > 0 and colIdx < len(grid[rowIdx])-1 and not flashed[rowIdx-1][colIdx+1]:
            grid[rowIdx-1][colIdx+1] += 1
          if rowIdx < len(grid)-1 and colIdx > 0 and not flashed[rowIdx+1][colIdx-1]:
            grid[rowIdx+1][colIdx-1] += 1
          if rowIdx < len(grid)-1 and colIdx < len(grid[rowIdx])-1 and not flashed[rowIdx+1][colIdx+1]:
            grid[rowIdx+1][colIdx+1] += 1
  return flashes

def step1():
  total = 0
  for i in range(100):
    total += advance_a_step(grid_1)
  print(total)


def step2():
  step = 0
  finished = False
  while not finished:
    advance_a_step(grid_2)
    step += 1
    if grid_2 == empty:
      break
  print(step)




step1()
step2()