table = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    0:0,
}

nums = input()

for c in nums:
    c = int(c)
    if  c in table:
        table[c] += 1
    else:
        table[c] = 1
smallest_n = 1000
smallest = 1
for i in range(10):
    if table[i] < smallest_n:
        smallest_n = table[i]
        smallest = i

# reset smallest to a different num if it is 0 and an equal count in a different number
if smallest == 0:
    break_again = False
    for i in range(9):
        num = i + 1
        if table[num] == table[0]:
            smallest = num
            break_again = True
            break
    zeros = ["1"]
    
if smallest == 0:
    for i in range(table[0]+1):
        zeros.append("0")
    zeros = "".join(zeros)
    print(zeros)

else:
    number = []
    for i in range(table[smallest]+1):
        number.append(str(smallest))
    number = "".join(number)
    print(number)