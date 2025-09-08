z = input().split()
k = int(z[0])
m = int(z[1])
n = int(z[2])

k-=m
k+=1
c=k%(m+n)
if c == 0:
    print("Barb")
elif c<=n:
    print("Alex")
else:
    print("Barb")