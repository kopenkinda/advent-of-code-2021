lines = []

with open('./10.input') as f:
  for line in f:
    lines.append(list(line.strip()))

def first_incorrect_closing(line):
  opened = []
  for char in line:
    if char == '(' or char == '[' or char == '{' or char == '<':
      opened.append(char)
    elif char == ')' and len(opened) > 0 and opened[-1] == '(':
      opened.pop()
    elif char == ']' and len(opened) > 0 and opened[-1] == '[':
      opened.pop()
    elif char == '}' and len(opened) > 0 and opened[-1] == '{':
      opened.pop()
    elif char == '>' and len(opened) > 0 and opened[-1] == '<':
      opened.pop()
    else:
      return char
  return None


def complete_line(line):
  opened = []
  for char in line:
    if char == '(' or char == '[' or char == '{' or char == '<':
      opened.append(char)
    elif char == ')' and len(opened) > 0 and opened[-1] == '(':
      opened.pop()
    elif char == ']' and len(opened) > 0 and opened[-1] == '[':
      opened.pop()
    elif char == '}' and len(opened) > 0 and opened[-1] == '{':
      opened.pop()
    elif char == '>' and len(opened) > 0 and opened[-1] == '<':
      opened.pop()
    else:
      return char
  closed = []
  for char in opened[::-1]:
    if char == '(':
      closed.append(')')
    elif char == '[':
      closed.append(']')
    elif char == '{':
      closed.append('}')
    elif char == '<':
      closed.append('>')
  return closed

def step1():
  result = 0
  for line in lines:
    char = first_incorrect_closing(line)
    if char is not None:
      if char == ')':
        result += 3
      if char == ']':
        result += 57
      if char == '}':
        result += 1197
      if char == '>':
        result += 25137
  print(result)


def step2():
  scores = []
  for line in lines:
    summ = 0
    char = first_incorrect_closing(line)
    if char is None:
      completed = complete_line(line)
      for character in completed:
        summ *= 5
        if character == ')':
          summ += 1
        if character == ']':
          summ += 2
        if character == '}':
          summ += 3
        if character == '>':
          summ += 4
      # print(''.join(completed), summ)
      scores.append(summ)
  scores = sorted(scores)
  print(scores[int(len(scores) /2)])


step1()
step2()