buns = [int(x) for x in input().split()[1:]]
dogs = [int(x) for x in input().split()[1:]]
dp_b = {0:0}; dp_d = {0:0}
i = -1
smallest = 1001

while i < len(buns) or i < len(dogs):
    i += 1

    # update buns
    if i < len(buns):
        new_b = {}

        # create a hash of every possible updated value from dp_b with the new i
        for cur_size in dp_b:
            # create hash entry
            if (cur_size + buns[i]) not in new_b: new_b[cur_size + buns[i]] = dp_b[cur_size] + 1
            # if one exists update if better
            if new_b[cur_size + buns[i]] > dp_b[cur_size] + 1: new_b[cur_size + buns[i]] = dp_b[cur_size] + 1

        # loop through hash and update dp_b as need
        for new_size in new_b:
            # if the size doesn't yet exist in dp_b
            if new_size not in dp_b: dp_b[new_size] = new_b[new_size]
            # otherwise check if it is a better solution
            elif dp_b[new_size] > new_b[new_size]: dp_b[new_size] = new_b[new_size]

        # # try updating smallest
        # if new_size in dp_d and smallest > (dp_d[new_size] + new_b[new_size]):
        #     smallest = dp_d[new_size] + new_b[new_size]            



    # update hotdogs
    if i < len(dogs):
        new_d = {}

        # create a hash of every possible updated value from dp_b with the new i
        for cur_size in dp_d:
            # create hash entry
            if (cur_size + dogs[i]) not in new_d: new_d[cur_size + dogs[i]] = dp_d[cur_size] + 1
            # if one exists update if better
            if new_d[cur_size + dogs[i]] > dp_d[cur_size] + 1: new_d[cur_size + dogs[i]] = dp_d[cur_size] + 1

        # loop through hash and update dp_b as need
        for new_size in new_d:
            # if the size doesn't yet exist in dp_b
            if new_size not in dp_d: dp_d[new_size] = new_d[new_size]
            # otherwise check if it is a better solution
            elif dp_d[new_size] > new_d[new_size]: dp_d[new_size] = new_d[new_size]

        # # try updating smallest
        # if new_size in dp_b and smallest > (dp_b[new_size] + new_d[new_size]):
        #     smallest = dp_b[new_size] + new_d[new_size]     

if len(dp_d) < len(dp_b):
    sm = dp_d
    lg = dp_b
else:
    sm = dp_b
    lg = dp_d
for key in sm:
    if key == 0:
        continue
    if key in lg and (lg[key] + sm[key]) < smallest: smallest = (lg[key] + sm[key])


# print(f"dp_b: {dp_b}\n")
# print(f"dp_d: {dp_d}\n")
if smallest == 1001: print("impossible")
else: print(smallest)