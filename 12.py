class Node:
    def __init__(self, name):
        self.name = name
        self.small = True
        if name.upper() == name:
            self.small = False
