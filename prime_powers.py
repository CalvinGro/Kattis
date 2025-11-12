import math
E = int(input())
L = int(input())
R = int(input())
MOD = (10**9)+7

arr = [1 for _ in range(R+1)]
arr[0], arr[1] = 0, 0
count = 1
primes_found = False
for i in range(2, int(math.sqrt(len(arr))+1)):
    if arr[i]: 
        j = i * i
        while j <= R:
            arr[j] = 0
            j += i


for i, b in enumerate(arr):
    if b and i >= L: count = (count*i)%MOD; primes_found = True

if not primes_found: print(1)

else: print(pow(count,E,MOD))