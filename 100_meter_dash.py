# from decimal import Decimal, getcontext
import math
# getcontext().prec = 40

def check_back(ref_points:list[tuple[float,float]], current:int) -> bool:
    meters = 0
    for i, point in enumerate(ref_points):
        if i > current:
            break
        meters += point[0]
        if meters >= 100:
            return True
    return False
    
def check_forward(ref_points:list[tuple[float,float]], current:int) -> bool:
    meters = 0
    for point in ref_points[current:]:
        meters += point[0]
    if meters >= 100:
        return True
    else:
        return False
        

def find_distance(x:float, y:float, prev_dist:tuple[float,float]) -> float:
    if x > prev_dist[0]:
        a = x-prev_dist[0]
    else:
        a = prev_dist[0] - x
    if y > prev_dist[1]:
        b = y-prev_dist[1]
    else:
        b = prev_dist[1]-y
    a = a*a
    b = b*b
    return math.sqrt(a+b) # (a+b).sqrt()

def refine_points(points:list[tuple[float,float,float]]) -> list[tuple[float,float]]:
    refined_points=[]
    prev_t = 0
    prev_dist = (0,0)
    for point in points:
        dist = find_distance(point[0], point[1], prev_dist)
        refined_points.append((dist, point[2]-prev_t))
        prev_dist = (point[0], point[1])
        prev_t = point[2]
    return refined_points


def find_fastest_100(ref_points:tuple[float,float]) -> float:
    fastest = float('inf')# Decimal("Infinity")

    for i,new_p in enumerate(ref_points):

        if check_back(ref_points, i):
            time = 0
            dist = 0
            for prev_p in ref_points[i::-1]:
                if dist >= 100:
                    break

                # if it can include the full segment
                elif (dist + prev_p[0]) < 100:
                    dist += prev_p[0]
                    time += prev_p[1]

                # adding part of a segment
                else:
                    ad_dist = 100 - dist
                    time += prev_p[1]*(ad_dist/prev_p[0])
                    dist += ad_dist
                    
            if time < fastest:
                fastest = time


        if check_forward(ref_points, i):
            time = 0
            dist = 0
            for new_p in ref_points[i:]:
                if dist >= 100:
                    break
                elif (dist + new_p[0]) < 100:
                    dist += new_p[0]
                    time += new_p[1]
                else:
                    ad_dist = 100 - dist
                    time += new_p[1]*(ad_dist/new_p[0])
                    dist += ad_dist
            if time < fastest:
                fastest = time

    return fastest



points=[]
a = int(input())
for i in range(a):
    points.append(input().split())
for point in points:
    point[0] = float(point[0])
    point[1] = float(point[1])
    point[2] = float(point[2])
refined_points = refine_points(points)
print(find_fastest_100(refined_points))


