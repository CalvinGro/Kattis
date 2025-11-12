# 4 2 1 2
# abcb
# cc
# c a
# 3
# 12
from bisect import bisect_right

la, lb, k, q = map(int, input().split())
A = input()
B = input()
lb = len(B)
skips = {} # how many skips each char of A will cause

count_b = {} # how many times each char occurs in B

indices = [0]*len(A) # how many skips occur during and before a certain index in a

A_indices = [0]*len(A)

a_bstrs = {}
A_sets = {} # occurances of a letter that must be removed

# make count_b
for c in B:
    if c in count_b: count_b[c] += 1
    else: count_b[c] = 1

# create skips
for i in range(k):
    a, b = input().split()
    # add case to A_set
    if a in A_sets: A_sets[a].add(b)
    else: A_sets[a] = {b}

    # add case to skips 
    if a in skips and b in count_b: skips[a] += count_b[b]
    elif b in count_b: skips[a] = count_b[b]
    
# build a_bstrs
for char in B:
    for key in A_sets:
        if char not in A_sets[key] and key not in a_bstrs: a_bstrs[key] = [char]
        elif char not in A_sets[key]: a_bstrs[key].append(char)

# build indices list
for i, c in enumerate(A):
    # if first char
    if i == 0: 
        if c not in skips: continue
        indices[0] = skips[c]; continue
    if c not in skips: indices[i] = indices[i-1]
    else: indices[i] = indices[i-1] + skips[c]
#print(indices)

# print(a_bstrs)
for i in range(1,len(A)):
    A_indices[i] = (i * lb * 2) - indices[i-1]*2
# print(f"A_indices: {A_indices}")

# taking in input for questions
for i in range(q):
    index = int(input())
    # print(f"index: {index}")
    # print(f"A_indices: {A_indices}")
    # index of a that that index is in
    best = bisect_right(A_indices, index)
    best -= 1
    # print(f"best: {best}")
    # print(f"A[best]: {A[best]}")
   
    cur = index - A_indices[best] # index in specific A str 

    # print(f"A_indices[best]: {A_indices[best]}")

    # print(f"A[best]: {A[best]}")
    # print(f"(cur-1)//2: {(cur-1)//2}")
    # print(f"best: {best}")
    # print(f"cur: {cur}")
    # print(f"a_bstrs[A[best]]: {a_bstrs[A[best]]}")
    # print(f"cur %2 == 0: {cur %2 == 0}")
    

    if cur % 2 == 0: print(A[best]) # GAY Silas code (Silas is gay)
    elif A[best] not in a_bstrs: print(B[((cur-1)//2)])
    else: print(a_bstrs[A[best]][((cur-1)//2)]) # cool code

  
