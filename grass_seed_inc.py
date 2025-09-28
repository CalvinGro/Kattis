c = float(input())

lawn_count = int(input())
total = 0
for i in range(lawn_count):
    l,w = input().split()
    total += c*(float(l) * float(w))
print(total)