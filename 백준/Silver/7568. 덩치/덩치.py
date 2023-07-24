import sys

n = int(input())
xy = []
rank_list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy.append((x, y))

for i in range(n):
    rank = 1
    for j in range(n):
        if xy[i] == xy[j]:
            continue
        elif xy[i][0] < xy[j][0] and xy[i][1] < xy[j][1]:
            rank += 1
    rank_list.append(rank)

print(*rank_list)