import sys

T = int(input())
lst = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    lst.append(a+b)

for i, value in enumerate(lst):
    print('Case #'+f'{i+1}: {value}')