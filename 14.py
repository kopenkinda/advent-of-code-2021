import math

pairs = {}
polymer = ''
polymer_pairs = {}


def get_pairs_from_polymer(polymer_str):
    pairs = {}
    for i in range(len(polymer_str) - 1):
        pair = polymer_str[i] + polymer_str[i + 1]
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs


with open('./14.input') as f:
    lines = [x.strip() for x in f.readlines()]
    polymer = lines.pop(0)
    lines.pop(0)
    lines = [x.split(' -> ') for x in lines]
    for pair in lines:
        pairs[pair[0]] = pair[1]
    polymer_pairs = get_pairs_from_polymer(polymer)


def advance_polymer(polymer):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += pairs[polymer[i] + polymer[i + 1]]
    new_polymer += polymer[-1]
    return new_polymer


def advance_polymer_pairs(polymer):
    new_polymer = {}
    for pair in polymer:
        count = polymer[pair]
        next = pairs[pair]
        left = pair[0] + next
        right = next + pair[1]
        new_polymer[left] = new_polymer.get(left, 0) + count
        new_polymer[right] = new_polymer.get(right, 0) + count
    return new_polymer


def step1():
    cpy = polymer
    for _ in range(10):
        cpy = advance_polymer(cpy)
    counts = {}
    for c in cpy:
        counts[c] = counts.get(c, 0) + 1
    max_v = max(counts.values())
    min_v = min(counts.values())
    print(max_v-min_v)


def step2():
    cpy = polymer_pairs
    for _ in range(40):
        cpy = advance_polymer_pairs(cpy)
    counts = {}
    for c in cpy:
        right, left = c
        counts[left] = counts.get(left, 0) + cpy[c]
        counts[right] = counts.get(right, 0) + cpy[c]
    for count in counts:
        counts[count] = math.ceil(counts[count] / 2)
    max_v = max(counts.values())
    min_v = min(counts.values())
    print(max_v-min_v)


step1()
step2()
