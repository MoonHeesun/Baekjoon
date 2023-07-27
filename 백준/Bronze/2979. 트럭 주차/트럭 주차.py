import sys

fee = list(map(int, sys.stdin.readline().split()))
parking = [0 for _ in range(100)]

for _ in range(3):
    arrive, leave = map(int, sys.stdin.readline().split()) 
    for i in range(arrive, leave):
        parking[i] = parking[i]+1

fee_total = 0
for h in parking:
    if h == 0:
        continue
    else:
        fee_total += fee[h-1]*h
print(fee_total)