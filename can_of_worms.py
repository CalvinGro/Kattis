# unsolved

import sys

lines = sys.stdin.buffer.read().splitlines()
n = int(lines[0])
checked = set()

class Node:

    def __init__(self, index, radius):
        self.index = index
        self.leftReach = -radius
        self.rightReach = radius
        self.children = []
        self.left = None
        self.right = None

    def rec_find_range(self) -> tuple[int, int]:
        # if already checked
        if self in checked: return (self.leftReach, self.rightReach)
        checked.add(self)

        

        





nodes = []  
for i, line in enumerate(lines[1:]):
    x, r = map(int, line.split())
    nodes.append(Node(x, r))

nodes.sort(key=lambda node: node.index)

# add left and right values
if len(nodes) == 1:
    for i, node in enumerate(nodes):
        if i == 0: node.right = nodes[i+1]
        elif i == len(nodes)-1: node.left = nodes[i-1]
        else: node.right = nodes[i+1]; node.left = nodes[i-1]


for node in nodes:
    if node not in checked:
        node.rec_find_range()



