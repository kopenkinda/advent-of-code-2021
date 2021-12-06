data = []
with open('./06.input') as f:
  data = list(map(int, f.readline().split(',')))

storage = {}

for el in data:
  if el not in storage:
    storage[el] = 0
  storage[el] += 1

days = 256

for _ in range(days+1):
  if _ == days - 1:
    counter = 0
    for index in storage:
      counter += storage[index]
  new_storage = {}
  for el in storage:
    if el == 0:
      if 6 not in new_storage:
        new_storage[6] = 0
      if 8 not in new_storage:
        new_storage[8] = 0
      new_storage[6] += storage[el]
      new_storage[8] += storage[el]
    else:
      if el - 1 not in new_storage:
        new_storage[el - 1] = 0
      new_storage[el - 1] += storage[el]
  storage = new_storage

print(counter)