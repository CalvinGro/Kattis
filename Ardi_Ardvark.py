class Node:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    
n, p = map(int, input().split())

head = Node()


for i in range(n):
    c, l = input().split(" ", 1)
    l = l.split()
    c = int(c)
    l_i = 0 # index of l
    node = head

    # handle one node at a time
    for _ in range(c):
        dir = l[l_i]
        ants = int(l[l_i+2])
        l_i += 4 

        if dir == 'L':
            if node.left: node = node.left; continue

            new_node = Node(ants)
            node.left = new_node
            node = new_node


        if dir == 'R':
            if node.right: node = node.right; continue        

            new_node = Node(ants)
            node.right = new_node
            node = new_node


# BUILT BT NOW CALC
sol = []

def dfs(node):
    left = 0; right = 0
    if node.left: left = dfs(node.left)
    if node.right: right = dfs(node.right)

    sol.append(min(left, right))
    return max(left, right) + node.val


sol.append(dfs(head))
sol.sort(reverse=True)
c = 0

for i in range(p):
    c += sol[i]
print(c)
    













