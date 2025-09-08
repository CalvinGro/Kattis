
def dist(x0,x1,y0,y1):
    dx = x1-x0
    dy = y1-y0
    return (dx**2+dy**2)**0.5


n = int(input())
segs = []
b = (0,0,0)
total_dist = 0

# create segs list.
# each segment is (total_distance, segment_distance, time)
for _ in range(n):     
    h = input().split()
    seg_dist = dist(float(b[0]),float(h[0]),float(b[1]),float(h[1]))
    total_dist += seg_dist
    # append (total_distance, segment_distance, time) for each segment
    segs.append((total_dist, seg_dist, float(h[2])-float(b[2])))
    b = h
i = 0
j = 100
next_i = 0
current_i = 0
next_j = 0


# find current_time
current_time = 0 
for seg in segs:
    if seg[0] < 100:
        current_time += seg[2]
    else:
        p = 100 - (seg[0]-seg[1])
        current_time += seg[2]*(p/seg[1])
        fastest = current_time
        break


for a, seg in enumerate(segs):
    if seg[0] >= 100:
        next_j = a
        break

# loop through segs and return fastest 
# segment once the end is reached.
while True:

    # if the distances to the next i and j points are both the same.
    if (segs[next_j][0] - 100) == segs[next_i][0]:
        dist_traveled = segs[next_i][0] - i
        if segs[next_j][1] != 0 and segs[current_i][1] != 0:
            current_time += (segs[next_j][2]*(dist_traveled/segs[next_j][1]))
            current_time -= (segs[current_i][2]*(dist_traveled/segs[current_i][1]))
        
        # check if current time is faster than fastest
        if current_time < fastest:
            fastest = current_time

        i+=dist_traveled
        j+=dist_traveled
        next_i+=1
        current_i+=1
        next_j+=1
        if next_j > n:
            print(fastest)
            break

    

    # if the next i point is closer.
    if segs[next_i][0]<(segs[next_j][0]-100):
        dist_traveled = segs[next_i][0]-i
        if segs[next_j][1] != 0 and segs[current_i][1] != 0:
            current_time += (segs[next_j][2]*(dist_traveled/segs[next_j][1]))
            current_time -= (segs[current_i][2]*(dist_traveled/segs[current_i][1]))

        # check if current time is faster than fastest
        if current_time < fastest:
            fastest = current_time

        i+=dist_traveled
        j+=dist_traveled
        next_i+=1
        current_i+=1
    

    # if the next j point is closer.
    if segs[next_i][0]>(segs[next_j][0]-100):
        dist_traveled = segs[next_j][0]-j
        if segs[next_j][1] != 0 and segs[current_i][1] != 0:
            current_time += segs[next_j][2]*(dist_traveled/segs[next_j][1])
            current_time -= segs[current_i][2]*(dist_traveled/segs[current_i][1])

        # check if current time is faster than fastest
        if current_time < fastest:
            fastest = current_time

        i+=dist_traveled
        j+=dist_traveled
        next_j+=1

        if next_j >= len(segs):
            print(fastest)
            break

        
        
        



