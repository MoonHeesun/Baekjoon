# import sys

# T = int(input())
# cbg = []
# def bfs(y, x, field):
#     direc = [1, -1]
#     for i in range(y):
#         for j in range(x):
#             if field[i][j] == 1:
#                 for d in direc:
#                     cbg.append([i+direc[d], j],[i, j+direc[d]])
#             else:
#                 continue
#     return field

# for i in range(T):
#     M, N, K = map(int, sys.stdin.readline().split())
#     field = [[0 for _ in range(M)] for _ in range(N)]
#     for i in range(K):
#         x, y = map(int, sys.stdin.readline().split())
#         field[y][x] = 1
#     field = bfs(y, x, field)
#     a = 0
#     for i in range(N):
#         for j in range(M):
#             a += field[i][j]
#         print(a, end=' ')

import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if 'push' in cmd:
        x = int(cmd[1])
        stack.append(x)
    elif 'pop' in cmd:
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif 'size' in cmd:
        print(len(stack))
    elif 'empty' in cmd:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in cmd:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])