gamma_rate = ''
epsilon_rate = ''
counters = []
with open('./03.input') as f:
    for line in f:
        for idx in range(len(line)):
            char = line[idx]
            if len(counters) <= idx:
                counters.append([0, 0])
            if char == '0':
                counters[idx][0] += 1
            else:
                counters[idx][1] += 1
counters.pop()

for counter in counters:
    if counter[0] > counter[1]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2

# oxy = 001
# co2 = 011
# 001
# 010
# 011

co2_scrubber_rating = ''
oxygen_generator_rating = ''
max_len = 0
least = []
most = []
with open('./03.input') as f:
    most_char = ''
    least_char = ''
    if counters[0][0] > counters[0][1]:
        most_char = '0'
        least_char = '1'
    else:
        most_char = '1'
        least_char = '0'
    co2_scrubber_rating += most_char
    oxygen_generator_rating += least_char
    for line in f:
        max_len = len(line)
        if line[0] == most_char:
            most.append(line)
        else:
            least.append(line)


def least_most_common(array, idx):
    #         '0''1'
    counter = [0, 0]
    for line in array:
        if line[idx] == '0':
            counter[0] += 1
        else:
            counter[1] += 1
    # [least, most]
    result = ['', '']
    if counter[0] == 0:
        return ['1', '1']
    if counter[1] == 0:
        return ['0', '0']
    if counter[0] > counter[1]:
        return ['1', '0']
    return ['0', '1']


least_most_idx = 1

while len(co2_scrubber_rating) < max_len:
    if len(most) <= 2 and len(least) <= 2:
        if len(most) == 1:
            co2_scrubber_rating = most[0]
        else:
            if most[0][max_len-1] == '1':
                co2_scrubber_rating = most[0]
            else:
                co2_scrubber_rating = most[1]
        if len(least) == 1:
            oxygen_generator_rating = least[0]
        else:
            if least[0][max_len-1] == '0':
                co2_scrubber_rating = least[0]
            else:
                co2_scrubber_rating = least[1]
        continue
    least_common = least_most_common(least, least_most_idx)[0]
    most_common = least_most_common(most, least_most_idx)[1]
    most = list(filter(lambda x: x[least_most_idx] == most_common, most))
    least = list(filter(lambda x: x[least_most_idx] == least_common, least))
    least_most_idx += 1

print(int(co2_scrubber_rating, 2) * int(oxygen_generator_rating, 2))
