from bisect import bisect_right
A_indices = [0, 4, 8, 12]
index = 1
while index != -1: 
    index= int(input())
    print(f"{bisect_right(A_indices, index)}\n")