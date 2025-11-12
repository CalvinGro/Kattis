m = int(input()); total = 0; prev = -1
for _ in range(m):
    n = int(input())
    # if 0
    if n == 0: 
        if prev == -1: continue
        prev = 0; continue
    # check if first number
    if prev == -1: total += n + 2; prev = n; continue
    # if fits in current bars
    if prev - n >= 0: prev = n; continue
    # otherwise
    total += 1 + n - prev; prev = n
print(total)