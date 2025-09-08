n,c,m = map(int, input().split())

nums = list(map(int, input().split()))
c= c-1
count = 0
been_before = []
while count <= n:
    if c >= n:
        print("right")
        print(count)
        break
    elif c < 0:
        print("left")
        print(count)
        break
    elif nums[c] == m:
        print("magic")
        print(count)
        break
    elif c in been_before:
        print("cycle")
        print(count)
        break
    else:
        been_before.append(c)
        c+=nums[c]
        count+=1
