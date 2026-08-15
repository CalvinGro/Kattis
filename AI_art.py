import math

x, y = input().split()
x = int(x)
y = int(y)

area_of_shapes = x*y/2

max_circ = (min(x,y)/2)**2 * 3.14159265
print(max_circ)
if max_circ >= area_of_shapes:
    # fits in circle
    print("circle")
elif 2*min(x, y) >= max(x, y):
    print("square")
else:
    print("blank")