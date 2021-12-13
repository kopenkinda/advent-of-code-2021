class Node:
    def __init__(self, name):
        self.name = name
        self.connections = set()
        self.small = True
        if name.upper() == name:
            self.small = False

    def connect(self, node):
        self.connections.add(node)


nodes = {}

with open('./12.input') as f:
    for line in f:
        sides = line.strip().split('-')
        converted = []
        for side in sides:
            node = Node(side)
            if side in nodes:
                node = nodes[side]
            converted.append(node)
            nodes[side] = node
        converted[0].connect(converted[1])
        converted[1].connect(converted[0])


def print_nodes():
    for node in nodes:
        current = nodes[node]
        print(current.name + "(" + str(current.small)+"): ", list(
            map(lambda x: x.name, current.connections)))


def get_paths(start_node):
    storage = []
    get_paths_inner(start_node, storage, [])
    return storage


def get_paths_inner(start_node, storage, traversed):
    traversed.append(start_node)
    if start_node.name == 'end':
        storage.append(traversed)
        return
    possible_new = []
    for connection in start_node.connections:
        if connection.small and connection in traversed:
            continue
        possible_new = [*traversed]
        get_paths_inner(connection, storage,  possible_new)


def get_paths2(start_node):
    storage = []
    get_paths_inner2(start_node, storage, [], False)
    return storage


def get_small(l):
    result = []
    for el in l:
        if el.small:
            result.append(el)
    return result


def get_paths_inner2(start_node, storage, traversed, double):
    traversed.append(start_node)
    if len(get_small(traversed)) > len(set(get_small(traversed))):
        double = True
    if start_node.name == 'end':
        storage.append(traversed)
        return
    for connection in start_node.connections:
        if connection.small:
            if connection in traversed and double:
                continue
            if connection.name == 'start':
                continue
        possible_new = [*traversed]
        get_paths_inner2(connection, storage, possible_new, double)


def step1():
    paths = get_paths(nodes['start'])
    print(len(paths))


def step2():
    paths = get_paths2(nodes['start'])
    print(len(paths))


step1()
step2()
