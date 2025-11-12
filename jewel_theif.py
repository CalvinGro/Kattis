# unfinished

# m = max weight
# n = count of items
n, m = [int(x) for x in input().split()]
# indices = [None]*(m+1)
best_values = [0]*(m+1)
for i in range(n):
    weight, value = [int(x) for x in input().split()]
    # print(f"\ncurrent weight: {weight}")
    # print(f"current value: {value}")
    # if best value for its weight add it there
    w = m - weight
    if weight > m:
        continue
    while w >= 0:
        # print(f"best_values: {best_values}")
        # print(f"trying w: {w} - {best_values[w]}")
        if best_values[weight+w] < (value + best_values[w]):
            best_values[weight+w] = (value + best_values[w])
            # print(f"indices[w]: {indices[w]}")
            
            # indices[weight+w] = [x for x in indices[w]]
            # indices[weight+w].append(i)
        w -= 1

# print(len(indices[-1]))
# for index in indices[-1]:
#     print(f"{index} ", end="")
# print()
for value in best_values[1:]:
    print(value, end=' ')
print()