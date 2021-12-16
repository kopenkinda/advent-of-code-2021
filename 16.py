packet_data = ""

with open('./16.input') as f:
    packet_data = bin(int(f.readline().strip(), 16))[2:]
    while len(packet_data) % 4 != 0:
        packet_data = '0' + packet_data


def parse_packet(storage, packet):
    if len(packet) < 7:
        return
    version = packet[0:3]
    is_operator = True
    type = packet[3:6]
    if type == "100":
        is_operator = False
    if is_operator:
        lt_ID = packet[6]
        packet = packet[7:]
        if len(packet) < 1:
            return
        if lt_ID == '0':
            next_packets_length = int(packet[:15], 2)
            subpackets = []
            packet = packet[15:]
            parse_packet(subpackets, packet[:next_packets_length])
            parse_packet(storage, packet[next_packets_length:])
            return storage.insert(0, {
                "is_operator": is_operator,
                "version": int(version, 2),
                "type": int(type, 2),
                "subpackets": subpackets,
            })
        else:
            next_packets_amount = int(packet[:11], 2)
            packet = packet[11:]
            subpackets = []
            parse_packet(subpackets, packet)
            storage.insert(0, {
                "is_operator": is_operator,
                "version": int(version, 2),
                "type": int(type, 2),
                "subpackets": subpackets[0:next_packets_amount],
            })
            return storage.extend(subpackets[next_packets_amount:])
    else:
        values = []
        rest = packet[6:]
        idx = 0
        while idx < len(rest):
            start = idx
            end = idx + 5
            current = rest[start:end]
            values.append(current[1:])
            if current[0] == "0":
                parse_packet(storage, rest[end:])
                break
            idx = end

        number = int(''.join(values), 2)

        return storage.insert(0, {
            "is_operator": is_operator,
            "version": int(version, 2),
            "type": int(type, 2),
            "number": number
        })


def evaluate(parsed_packet):
    if parsed_packet['is_operator']:
        if parsed_packet['type'] == 0:
            values = map(evaluate, parsed_packet['subpackets'])
            return sum(values)
        elif parsed_packet['type'] == 1:
            values = map(evaluate, parsed_packet['subpackets'])
            result = 1
            for v in values:
                result *= v
            return result
        elif parsed_packet['type'] == 2:
            values = map(evaluate, parsed_packet['subpackets'])
            return min(values)
        elif parsed_packet['type'] == 3:
            values = map(evaluate, parsed_packet['subpackets'])
            return max(values)
        elif parsed_packet['type'] in (5, 6, 7):
            left = evaluate(parsed_packet['subpackets'][0])
            right = evaluate(parsed_packet['subpackets'][1])
            if parsed_packet['type'] == 5:
                return 1 if left > right else 0
            if parsed_packet['type'] == 6:
                return 1 if left < right else 0
            if parsed_packet['type'] == 7:
                return 1 if left == right else 0
        else:
            raise Exception("Unknown operator type")
    else:
        return parsed_packet['number']


def version_sum(parsed_packets):
    result = 0
    for packet in parsed_packets:
        result += packet["version"]
        if packet['is_operator']:
            result += version_sum(packet['subpackets'])
    return result


def step1():
    storage = []
    parse_packet(storage, packet_data)
    result = version_sum(storage)
    print(result)


def step2():
    storage = []
    parse_packet(storage, packet_data)
    result = list(map(evaluate, storage))
    print(result[-1])


step1()
step2()
