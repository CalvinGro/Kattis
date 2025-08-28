from decimal import Decimal

def find_distance(x:Decimal, y:Decimal, prev_dist:tuple[Decimal,Decimal]) -> Decimal:
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
    return (a+b).sqrt()


x = Decimal(input())
y = Decimal(input())
a = Decimal(input())
b = Decimal(input())
prev_dist = (a,b)
print(find_distance(x,y,prev_dist))