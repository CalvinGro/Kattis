t = int(input())

for i in range(t):
    x = input().split()
    n = int(x[0])
    m = int(x[1])

    k=[]
    for j in range(n):
        k.append(0)
        k[j] = input()

    output = []
    for j in range(m):
        count = 0
        for l in k:
            count += int(l[j])
        if (count / n) >= 0.5:
            output.append(1)
        else:
            output.append(0)
    for o in output:
        print(o, end="")
    print()

