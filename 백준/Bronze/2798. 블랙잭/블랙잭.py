import sys

N, M = map(int, sys.stdin.readline().split(' '))
N_lst = list(map(int, sys.stdin.readline().split(' ')))

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = N_lst[i] + N_lst[j] + N_lst[k]
            if sum > M or sum < result:
                continue
            result = sum

print(result)