E, S, M = map(int, input().split())

year = []
e, s, m = 0, 0, 0
for i in range(1, 10000):
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    if E == e and S == s and M == m:
        year.append(i)

print(min(year))
    
