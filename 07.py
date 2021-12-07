with open('./07.input') as f:
  data = list(map(int, f.readline().split(',')))

def step1(data):
  minimum = min(data)
  maximum = max(data)
  costs = []
  for i in range(minimum, maximum+1):
    costs.append(sum([abs(i - x) for x in data]))
  return min(costs)


def step2(data):
  minimum = min(data)
  maximum = max(data)
  costs = []
  for i in range(minimum, maximum+1):
    costs.append(0)
    for el in data:
      range_start = i if el > i else el
      range_end = (el if el > i else i)
      diff = range_end - range_start
      costs[i] += sum(range(diff + 1))
  return min(costs)

print(step1(data))
print(step2(data))
