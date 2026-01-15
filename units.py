from collections import deque

n = 1
while n:
    n = int(input())

    _ = input()
    order = deque()

    conv = input().split()
    deque.append((conv[0], int(conv[2]), conv[3]))

    for i in range(n-1):
        
        
