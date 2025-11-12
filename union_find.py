# unsolved

import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

n, q = int(next(it)), int(next(it))

par = [i for i in range(n)]
rank = [1] * n



def find(n1):
    if n1 != par[n1]:
        par[n1] = find(par[n1])
    return par[n1]


def union(n1, n2):
    
    p1, p2 = find(n1), find(n2)
    
    if p1 == p2: return

    if rank[p1] > rank[p2]:
        rank[p1] += rank[p2]
        par[p2] = p1

    else:
        rank[p2] += rank[p1]
        par[p1] = p2
    return


for _ in range(q):
    op = next(it).decode() 
    n1, n2 = int(next(it)), int(next(it))
    n1 = int(n1); n2 = int(n2)

    if op == "=":
        union(n1,n2)
    
    else:
        p1, p2 = find(n1), find(n2)
        if p1 == p2: print("yes") 
        else: print("no")
