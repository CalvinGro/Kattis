
# get input
m = int(input())

prices = [int(x) for x in input().split()]
prices.reverse()

output = ["infinity"]
lowests = [prices[0]]
indices = {prices[0]: m}


def binary_search(price):
    a = 0
    b = len(lowests)-1
    c = b // 2
    while b - a > 1:
        # set middle value
        c = a + (b // 2)

        # if found return
        if price == lowests[c]:
            
            return price
        
        elif price > lowests[c]:
            b = c
        
        else:
            a = b

    if lowests[b] <= price: return lowests[b]
    else: return lowests[a]
        

# main loop
for price in prices[1:]:

    m -= 1
    # if new lowest
    if price < lowests[-1]:
        lowests.append(price)
        indices[price] = m
        output.append("infinity")
        continue

    # otherwise BS to find price it fits in
    prev = binary_search(price, m)

    output.append(indices[prev]-m)

output.reverse()

for out in output:
    print(out)
