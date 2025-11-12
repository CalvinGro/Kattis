# unsolved

import sys
from queue import Queue
data = sys.stdin.buffer.read().split(b'\n')

buses = 0; islands = 0; bridges = 0
maps = []
cur = []
unions = []

# r and c of the first "X"
def dfs_islands(cur) -> int:
    q = Queue()
    count = 0
    types = {"#","X"}
    for r in range(len(cur)):
            for c in range(len(cur[0])):
                if cur[r][c] in types:
                    count += 1
                    q.put((r,c))
                    currentQ = set()
                    currentQ.add((r,c))

                    # search all surrounding area
                    while not q.empty():
                        r, c = q.get()
                        if cur[r][c] ==  "#": cur[r][c] = "." # set current location to result type
                        else: cur[r][c] = count
                        if r != 0 and cur[r-1][c] in types and (r-1,c) not in currentQ: q.put((r-1,c)); currentQ.add((r-1,c))
                        if c != 0 and cur[r][c-1] in types and (r,c-1) not in currentQ: q.put((r,c-1)); currentQ.add((r,c-1))
                        if r != len(cur)-1 and cur[r+1][c] in types and (r+1,c) not in currentQ: q.put((r+1,c)); currentQ.add((r+1,c))
                        if c != len(cur[0])-1 and cur[r][c+1] in types and (r,c+1) not in currentQ: q.put((r,c+1)); currentQ.add((r,c+1))
    
    return count


def dfs_bridges(cur) -> int:
    count = 0
    for r in range(len(cur)):
            for c in range(len(cur[0])):
                if cur[r][c] == "B":
                    count += 1
                    cur[r][c] = "."

                    # if bridge extends across column
                    if r != 0 and r != len(cur)-1 and cur[r-1][c] != ".":
                        up = r-1
                        down = r+1
                        while up >= 0 and cur[up][c] == "B": cur[up][c] = "."; up -= 1
                        while down < len(cur) and cur[down][c] == "B": cur[down][c] = "."; down += 1
                        unions.append((cur[up][c], cur[down][c]))
                        

                    # if bridge extends across row
                    else:
                        left = c-1
                        right = c+1
                        while left > 0 and cur[r][left] == "B": cur[r][left] = "."; left -= 1
                        while right < len(cur[0]) and cur[r][right] == "B": cur[r][right] = "."; right += 1
                        unions.append((cur[r][left], cur[r][right]))
                     
    
    return count    


def find(n, par):
    while n != par[n]:
        par[n] = par[par[n]]
        n = par[n]
    return par[n]
     


for line in iter(data):
    line = line.decode()

    # if end of current map reached
    if line == "": # if len(line) != cur_len and cur !=[]: 
        unions = []
        islands = dfs_islands(cur)
        bridges = dfs_bridges(cur)

        buses = [i for i in range(islands+1)]
        for n1, n2 in unions:
            if n1 == "." or n2 == ".": continue
            p1, p2 = find(n1, buses), find(n2, buses)

            if p1 == p2: continue
            buses[p1] = p2
        
        count = -1
        
        for i, bus in enumerate(buses):
            if bus == i: count += 1
            

        # add to maps 
        maps.append((count, islands, bridges))
        cur = []
        continue

    # build new line of map
    cur.append(list(line))

i = 0
for m in maps:
    i += 1

    print(f"Map {i}")
    print(f"islands: {m[1]}")
    print(f"bridges: {m[2]}")
    print(f"buses needed: {m[0]}")
    print()



    
    
    
