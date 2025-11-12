# unfinished

i = 0
j = int(input())
tasks = []
for _ in range(j):
    a, b = input().split()
    a = int(a)
    b = int(b)
    tasks.append((a-b,a,b))
tasks.sort()
print(tasks)
a_total = 0
b_total = 0
j -= 1
count = 1
while i<j:
    print(f"\ncount: {count}")
    print(f"i: {i}")
    print(f"j: {j}")
    print(f"a_total: {a_total}")
    print(f"b_total: {b_total}")
    count += 1
    if a_total + tasks[i][1] <= b_total + tasks[j][2]:
        a_total += tasks[i][1]
        i+=1
    else:
        b_total += tasks[j][2]
        j-=1

print(f"\nFinal, once i == j")
if a_total + tasks[i][1] <= b_total + tasks[j][2]:
    a_total += tasks[i][1]
else:
    b_total += tasks[j][2]
print(f"i: {i}")
print(f"j: {j}")
print(f"a_total: {a_total}")
print(f"b_total: {b_total}")
if a_total > b_total:
    print(a_total)
else:
    print(b_total)
    

    