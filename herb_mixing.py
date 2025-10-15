g, r = input().split()
total = 0
g = int(g)
r = int(r)

total += (min(r,g)*10)
g = g - r
i = 3
point_values = [0,1,3,10]

while g > 0 and i > 0:
    total += (g // i) * point_values[i]
    g = g % i
    i -= 1
print(total)