n = int(input())

def dist(x0,x1,y0,y1):
    dx = x1-x0
    dy = y1-y0
    return (dx**2+dy**2)**0.5

segments = []
b = [0,0,0]

rund = 0
runt = 0

rund2 = 0
runt2 = 0

save = 0
final = 10**8

bsave = 0
brund = 0
brunt = 0

for i in range(n):
    x = False
    if rund <100:
        h = input().split()
   
        if i<(n):
            segments.append([])
            segments[i].append(dist(float(b[0]),float(h[0]),float(b[1]),float(h[1])))
            segments[i].append(float(h[2])-float(b[2]))
            b = h
            x = True
            brund+=segments[i][0]
            brunt+=segments[i][1]
        rund+=segments[i][0]
 
    else:
        i-=1
       
    if x:
        while brund>=100:
            brund-=segments[bsave-1][0]
            brunt-=segments[bsave-1][1]
            if bsave<=i:
                bsave+=1
       
        if bsave>1:
            brund+=segments[bsave-1][0]


        if brund>=100:
            p = brund-100
            bprop = 1-(p/segments[bsave-1][0])
            brunt += segments[bsave-1][1]*bprop
            if brunt<final:
                final = brunt
            
            brunt -= segments[bsave-1][1]*bprop
            brunt+=segments[bsave-1][1]
   
    if rund >= 100:
        s = 100-rund2
        prop = s/segments[i][0]
        runt += segments[i][1]*prop

        if runt<final:
            final = runt

        runt -= segments[i][1]*prop
        rund -= segments[save][0]
        runt -= segments[save][1]
        save+=1

    if rund<100:
        runt+= segments[i][1]
       
       
    rund2 = rund
   
print(final) 
