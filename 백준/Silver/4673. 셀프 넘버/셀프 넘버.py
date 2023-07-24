array = [i for i in range(1,10001)]

for start in range(1, 10001):
    share = start
    d = 0
    while share != 0:
        rest = share%10
        share = share//10
        d += rest
    next = start+d+share
    if next in array:
        array.remove(next)
    else:
        continue

for i in array:
    print(i)