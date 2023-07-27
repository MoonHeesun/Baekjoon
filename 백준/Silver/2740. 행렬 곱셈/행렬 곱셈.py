import sys

N, M = map(int, sys.stdin.readline().split())
a = []
for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    a.append(x)

M, K = map(int, sys.stdin.readline().split())
b = []
for i in range(M):
    y = list(map(int, sys.stdin.readline().split()))
    b.append(y)

mul = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            mul[n][k] += a[n][m]*b[m][k]

for i in range(N):
    for j in range(K):
        print(mul[i][j], end=' ')
    print()
