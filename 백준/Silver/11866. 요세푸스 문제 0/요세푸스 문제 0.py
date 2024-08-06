from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split(' '))
circle = deque()

for i in range(1, N+1):
    circle.append(i)

permutation = []
while len(circle) != 0:
    circle.rotate(-(K-1))
    num = circle.popleft()
    permutation.append(num)

print("<", end='')
print(*permutation, sep=', ', end='')
print(">")