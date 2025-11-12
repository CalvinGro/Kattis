
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# create dp of sets
dp_sets = {}; num = 0; loops = []; loop_nums = {}; loops_i = 0
for point in nums:
    
    num += 1
    # print(f"\n___for num {num}___")
    # print(f"dp_sets: {dp_sets}")
    # print(f"loops: {loops}")
    # print(f"loop_nums: {loop_nums}")
    # print(f"point: {point}")
    # if the number points to a loop
    if point in loop_nums:
        # print(f"point: {point} in loop_nums")
        # add 1 to the max in the tuple for that loop
        # print(f"loops: {loops}")
        # print(f"loop_nums[point]: {loop_nums[point]}")
        add_val = 1
        if num in dp_sets: 
            for n in dp_sets.pop(num):
                loop_nums[n] = loop_nums[point]
                add_val += 1

        loops[loop_nums[point]][1] += add_val
        loop_nums[num] = loop_nums[point] # add current number to loop_nums
        continue

    # if the number points to itself add it to loops and loop_nums
    if point == num: 
        mx = 1
        # if the number is a key in dp_sets
        if num in dp_sets:
            for n in dp_sets.pop(num): loop_nums[n] = loops_i; mx += 1


        loops.append([1,mx]); loop_nums[num] = loops_i; loops_i += 1; continue

    # if the point is not in a set yet
    point_set = None

    # else find the set it is in and set point_set equal to its key
    if point < num: 
        for dp_key in dp_sets: 
            if point in dp_sets[dp_key]: point_set = dp_key
    
    # print(f"point_set: {point_set}")

    # if the number is the key to a current dp_set
    if num in dp_sets:

        # but the point is not in a dp_set
        if point_set is None:
            # if point is not a key in dp_sets
            if not point in dp_sets: dp_sets[point] = dp_sets.pop(num); dp_sets[point].add(num)
            # if point is a key in dp_sets
            else: dp_sets[point].update(dp_sets.pop(num)); dp_sets[point].add(num)

        # if the point is in the same dp_set add it to loops and add all nums to loop_nums
        elif point_set == num:
            # print("\ncreating new loop entry:")
            # create pop_set and remove the set from dp_sets
            pop_set = dp_sets.pop(num); pop_set.add(num)

            # find min of loop
            mn = 1; cur = point
            # print(f"point: {point}")
            # print(f"num: {num}")
            while cur != num: cur = nums[cur-1]; mn += 1
            # print(f"mn: {mn}\n")

            # add loops min and max to loops
            loops.append([mn,len(pop_set)])
            
            # add all the nums in the set to loop_nums at loops_i and inc loops_i
            for n in pop_set: loop_nums[n] = loops_i
            loops_i += 1

        # else if the point is in a different set merge the sets
        else:
            dp_sets[point_set].update(dp_sets.pop(num))
            dp_sets[point_set].add(num)


    else:
        # if neither point or num are in loop_nums or dp_sets, create new set
        if point_set is None: 
            if not point in dp_sets: dp_sets[point] = {num}
            else: dp_sets[point].add(num)

        # otherwise just add it to its respective set
        else: dp_sets[point_set].add(num)

# print(f"\n___halfway___")
# print(f"dp_sets: {dp_sets}")
# print(f"loops: {loops}")


# ONCE LOOPS IS FULLY CREATED

largest = 0; ranges = {(0,0)}; done = False
for (min, max) in loops:
    # print(f"\n for ({min}, {max}):")
    new_ranges = set()
    for tup in ranges:
        new_tup = (tup[0]+min, tup[1]+max)
        # print(f"new_tup: {new_tup}")
        # print(f"ranges: {ranges}")
        # if range past k skip 
        if k < new_tup[0]: continue

        # break if k found in range
        elif k >= new_tup[0] and k <= new_tup[1]: done = True; print(k); break

        # update largest
        elif new_tup[1] > largest: largest = new_tup[1]
        new_ranges.add(new_tup)
    ranges.update(new_ranges)

    if done: break

# if exact k not found
if not done: print(largest)

    
# print(f"\n___Final___")

# print(f"loops: {loops}\n")
# print(f"ranges: {ranges}\n")
# print(f"loop_nums: {loop_nums}\n")

            

        


    

