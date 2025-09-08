x = input().split()

n = int(x[0])
pgiven = int(x[1])
pneed = int(x[2])

for i in range(n):
    a = int(input())
    print(round(a*(pneed/pgiven)))