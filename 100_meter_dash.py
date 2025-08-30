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
            print(f"Dist: {segments[i][0]}")
            print(f"Time: {segments[i][1]}")
            print(f"Brund with new seg: {brund}")
            print(f"Brunt with new seg: {brunt}")
        rund+=segments[i][0]
 
    else:
        i-=1
       
    if x:
        while brund>=100:
            brund-=segments[bsave-1][0]
            brunt-=segments[bsave-1][1]
            print(f"brund subtracting: {segments[bsave-1][0]}")
            print(f"brund: {brund}")
            print(f"prev bsave: {bsave}")
            if bsave<=i:
                bsave+=1
                print(f"new bsave: {bsave}\n")
       
        if bsave>1:
            print(f"brund: {brund}")
            brund+=segments[bsave-1][0]
            print(f"adding {segments[bsave-1][0]}")
            print(f"new brund: {brund}")


        if brund>=100:
            p = brund-100
            print(f"brund: {brund}")
            bprop = 1-(p/segments[bsave-1][0])
            brunt += segments[bsave-1][1]*bprop
            if brunt<final:
                print("NEW FINAL\n")
                final = brunt
            print(f"Tried: {brunt}\n_______\n\n")
            
            brunt -= segments[bsave-1][1]*bprop
            brunt+=segments[bsave-1][1]
        else:
            print("Brund < 100\n_______\n\n")
   
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
   
   
   
print("\n\n",final)    
