n = int(input())

printers = 1
day = 1
while printers < n:
    printers *= 2 
    day += 1
print(day)
