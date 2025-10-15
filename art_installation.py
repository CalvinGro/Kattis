needed = [int(x) for x in input().split()]
have = [int(x) for x in input().split()]
shop = [int(x) for x in input().split()]
count = 0
# subtract what we have
for i in range(3):
    needed[i] -= have[i]
    if needed[i] < 0:
        needed[i] = 0

# check red
if shop[0] < needed[0]:
    # not enough red
    print(-1)
else:
    count += needed[0]
    shop[0] -= needed[0]

    # check blue
    if shop[1] < needed[2]:
        # not enough blue
        print(-1)
    else:
        count += needed[2]
        shop[1] -= needed[2]

        # check green
        if (shop[0] + shop[1]) < needed[1]:
            print(-1)
        else:
            print(count + needed[1])