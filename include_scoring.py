
# STEP 1 - input and build top 30

n = int(input()); entries = []
# top 30 best scores not necessarly top 30 players tho
top = [set() for _ in range(30)]

def compare(l1, l2):
    if l1[0] > l2[0]: return 0
    elif l2[0] > l1[0]: return 1
    elif l1[1] < l2[1]: return 0
    elif l2[1] < l1[1]: return 1
    elif l1[2] < l2[2]: return 0
    elif l2[2] < l1[2]: return 1
    return -1

def add_to_top(entry):
    # if rank 30 is filled and rank 30 is better than the entry return
    if len(top[29]) != 0 and compare(entries[entry], entries[next(iter(top[29]))]) == 1: return

    # check if tied with val in rank                                 
    for i_set in top:
        # sense cmprs are starting from the left, if a len 0 is reach the rest are 0
        if len(i_set) == 0: break
        # check any rank has the same exact score; if so simply simply add the entry to that rank and return
        if compare(entries[next(iter(i_set))], entries[entry]) == -1: i_set.add(entry); return

    # rm rank 30
    top.pop(-1)

    # compare to all the ranks and find its place
    for i, i_set in enumerate(top[::-1]):
        
        # skip past all empty entries
        if len(i_set) == 0: continue
        
        # if the entry is worse insert it at the prev index
        if compare(entries[next(iter(i_set))], entries[entry]) == 0: top.insert(len(top)-i, {entry}); return
    
    # if better than all current ranks
    top.insert(0, {entry})
    return

# create top 30 list and add all entries to list
for i in range(n):
    entries.append([int(x) for x in input().split()])
    add_to_top(i)

# STEP 2 - assign points

# create hash for ranks indices to there point values
ranks = {}
points = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
p = 0 # points index
for rank in top:

    # if there are less than 30 elements
    if len(rank) == 0: break

    total = 0
    # get total points 
    for n in range(len(rank)):
        # if all points taken its done
        if p == len(points): break
        total += points[p]
        p += 1
    individual_points = -(-total//len(rank))

    # make ranks entry for every index at that rank
    for index in rank: ranks[index] = individual_points

# final print
for i, entry in enumerate(entries):
    num = entries[i][3]
    if i in ranks: num += ranks[i]
    print(num)