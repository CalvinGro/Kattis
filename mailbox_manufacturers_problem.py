totals = []
total = 0

for i in range(90, 95):
    total += i
    totals.append(i)
print(totals)
print(f"total: {total}")
n_total = 0
m = 0  
n = 3
print(totals[n])
m_total = 0
while n > m:
    if m_total >= n_total:
        n_total += totals[n]
        print(f"n added: {totals[n]}")
        n-=1
    else:
        m_total += totals[m]
        print(f"m added: {totals[m]}")
        m+=1
print(f"guess: {totals[n]}")
print(f"n: {n}")
print(f"m: {m}")
print(f"n_total: {n_total}")
print(f"m_total: {m_total}")
    