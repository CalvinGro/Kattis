cost = int(input().split()[1])
items = list(map(int, input().split()))
items.sort()
broke_out = False
for i, item in enumerate(items[1:], start=1):
    if (item + items[i-1]) > cost:
        print(i)
        broke_out = True
        break

if not broke_out:
    print(len(items))


