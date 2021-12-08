initial_data = []

with open('./08.input') as f:
  for line in f:
    line = line.strip()
    if line:
      initial_data.append(list(map(lambda x: list(map(lambda y: sorted(list(y)), x.split(' '))), line.split(' | '))))

def includes(src, tgt):
  for c in src:
    if c not in tgt:
      return False
  return True

transformed_data = []

for i in initial_data:
  digits = {}
  left = i[0]
  right = i[1]
  passes = 0
  while len(digits) < 10:
    passes += 1
    for j in left:
      if len(j) == 2:
        digits[1] = j
      if len(j) == 3:
        digits[7] = j
      if len(j) == 4:
        digits[4] = j
      if len(j) == 7:
        digits[8] = j
      try:
        if len(j) == 6:
          if includes(digits[4], j):
            digits[9] = j
          if not includes(digits[1], j):
            digits[6] = j
          if includes(digits[7], j) and not includes(digits[4], j):
            digits[0] = j

        if len(j) == 5:
          if includes(j, digits[9]) and includes(digits[1], j):
            digits[3] = j
          if includes(j, digits[6]):
            digits[5] = j
          if j != digits[5] and j != digits[3]:
            digits[2] = j

      except KeyError:
        pass
  digits['data'] = right
  transformed_data.append(digits)

def step1(digits_arr):
  counter = 0
  for digits in digits_arr:
    for i in digits['data']:
      for k in digits:
        if i == digits[k]:
          if k == 1 or k == 4 or k ==7 or k ==8:
            counter += 1
  print(counter)


def step2(digits_arr):
  counter = 0
  for digits in digits_arr:
    scale = 1000
    for i in digits['data']:
      for k in digits:
        if i == digits[k]:
          counter += k * scale
          scale /= 10
  print(int(counter))

step1(transformed_data)
step2(transformed_data)