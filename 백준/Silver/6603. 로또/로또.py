import sys

def fn(depth, i):
    if depth == 6:
        print(*res, end='\n')
        return
    for j in range(i, k):
        res[depth] = s[j]
        fn(depth+1, j+1)

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s[0]
    res = [0 for _ in range(6)]
    if k == 0:
        break
    else:
        del s[0]
        s = sorted(s)
    fn(0, 0)
    print()