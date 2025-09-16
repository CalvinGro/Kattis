import sys

for line in sys.stdin:
    a,b = line.split()
    a = int(a)
    b = int(b)
    if a > b:
        print(int(a) - int(b))
    else:
        print(int(b) - int(a))
