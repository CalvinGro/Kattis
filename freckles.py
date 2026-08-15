# unfinished

import math 

def find_dist(x1, y1, x2, y2):
    return math.sqrt((x1+x2)**2 + (y1 + y2)**2)


n = int(input())
_ = input()

# create set of points not currently in the union
points = set()
for _ in range(n): 
    points.add(( tuple(map(float, input().split())) ))

cur = points.pop()

while len(points) != 0:
    lowest = 100_000_000
    
    
    