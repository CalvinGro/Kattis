
# unfinished
last = int(input())
papers = list(map(int, input().split()))

w = 2 ** (-5 / 4)
h = 2 ** (-3 / 4)

total_tape = h

i = 2
impossible = True
c = 0

while c < len(papers):
    i -= papers[c]

    if i <= 0:
        impossible = False
        break
    
    total_tape += w * i # mult by widths

    temp_h = h
    h = w
    w = temp_h/2

    i *= 2
    c += 1
if impossible:
    print("impossible")
else:
    print(total_tape)