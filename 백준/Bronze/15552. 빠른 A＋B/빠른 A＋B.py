import sys

T = int(input())
lst = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split(' '))
    lst.append(a+b)

for i in lst:
    print(i)