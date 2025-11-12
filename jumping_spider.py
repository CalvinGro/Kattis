from queue import Queue
R, C = [int(i) for i in input().split()]

grid = []
# create legs grid
for r in range(R):
    grid.append([int(i) for i in input().split()])


for r in range(R):
    for c in range(C):
        if grid[r][c] > 0: # add to all surrounding in legs
            around = []
            checked = {(r,c)}
            arq = Queue()
            arq.put((r,c,0))
            while not arq.empty():
                r, c, d = arq.get()
                if d < 3:
                    if r != 0 and (r-1,c) not in checked:
                        arq.put((r-1,c,d+1))
                        checked.add((r-1,c))
                        around.append((r-1,c))
                    if r != R-1 and (r+1,c) not in checked:
                        arq.put((r+1,c,d+1))
                        checked.add((r+1,c))
                        around.append((r+1,c))

                    if c != 0 and (r,c-1) not in checked:
                        arq.put((r,c-1,d+1))
                        checked.add((r,c-1))
                        around.append((r,c-1))
                    if c != C-1 and (r,c+1) not in checked:
                        arq.put((r,c+1,d+1))
                        checked.add((r,c+1))
                        around.append((r,c+1))
                
            for nr, nc in around:
                if grid[nr][nc] > 0: grid[nr][nc] += 1

# calc groups
groups = 0; others = 0
Q = Queue()
Qset = set()


for r in range(R):
    for c in range(C):
        if grid[r][c] == 0: continue
        
        if grid[r][c] > 7:
            Q.put((r,c)); Qset.add((r,c)); groups += 1
            while not Q.empty():
                r,c = Q.get()
                grid[r][c] = 0


                around = [(r,c)]
                checked = {(r,c)}
                arq = Queue()
                arq.put((r,c,0))
                while not arq.empty():
                    r, c, d = arq.get()
                    if d < 3:
                        if r != 0 and (r-1,c) not in checked:
                            arq.put((r-1,c,d+1))
                            checked.add((r-1,c))
                            around.append((r-1,c))

                        if r != R-1 and (r+1,c) not in checked:
                            arq.put((r+1,c,d+1))
                            checked.add((r+1,c))
                            around.append((r+1,c))

                        if c != 0 and (r,c-1) not in checked:
                            arq.put((r,c-1,d+1))
                            checked.add((r,c-1))
                            around.append((r,c-1))

                        if c != C-1 and (r,c+1) not in checked:
                            arq.put((r,c+1,d+1))
                            checked.add((r,c+1))
                            around.append((r,c+1))

                    
                for nr, nc in around:
                    if grid[nr][nc] > 0:
                        Qset.add((nr,nc)); Q.put((nr,nc))
                    # elif grid[nr][nc] > 0:
                    #     Qset.add((nr,nc)); grid[nr][nc] = 0




for r in range(R):
    for c in range(C):
        if grid[r][c] > 0: others += 1

# Final
if groups > 0: print("Yes"); print(groups-1)
else: print("No"); print(0)
print(others)
