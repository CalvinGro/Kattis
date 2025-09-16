import sys


sys.setrecursionlimit(400000)


def _recursive_build_list(i, recently_added, prev_i):
    if isinstance(n[i], int):
        prev = i + n[i]
        if prev < 0 or prev > len(n)-1:
            prev = -1
        new_recents = recently_added
        new_recents.append(i)

        # if there is no prev_i cause its the first value
        if prev_i != -1:
            n[i] = [0, [prev_i], prev]
        else:
            n[i] = [0, [], prev]

        # checking for loops
        if prev in recently_added:
            index = 0 
            for j in recently_added:
                if j == prev:
                    break
                else:
                    index += 1
            loops.append(new_recents[index:])
            n[prev][1].append(i)
        
        elif  prev != -1:
            _recursive_build_list(prev, new_recents, i)
    else:
        # if another already formed node(tuple) is reached
        # add the previous node to the list of those that point at it.
        if prev_i != -1:
            n[i][1].append(prev_i)


def _recursive_find_values(i, lineage, cur_adjuster):
    updated_lineage = lineage
    updated_lineage.append(i)
    n[i][0] -= cur_adjuster
    cur_adjuster += 1
    if len(n[i][1]) == 0:
        for node_i in updated_lineage:
            n[node_i][0] += cur_adjuster
    else:
        for node_i in n[i][1]:
            _recursive_find_values(node_i,updated_lineage, 0)

# take input
m = int(input())
n = list(map(int, input().split()))
loops = []
total = 0

# build n 
for i in range(len(n)):
    _recursive_build_list(i, [], -1)

for loop in loops:
    for node_i in loop:
        if len(n[node_i][1]) > 1:
            for next_node_i in n[node_i][1]:
                if next_node_i not in loop:
                    _recursive_find_values(next_node_i, [], 0)
        else:
            n[node_i][0] += 1

for loop in loops:
    sum = 0
    for node_i in loop:
        sum += n[node_i][0]
    for node_i in loop:
        n[node_i][0] = sum

tmp_count = 0
for i in range(len(n)):
    tmp_count += 1
    if n[i][0] == 0:
        _recursive_find_values(i, [], 0)


for node in n:
    total += node[0]
print(total)


        