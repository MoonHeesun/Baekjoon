from collections import deque
import sys

n = int(input())
queue = deque([])

for i in range(n):
    cmd = list(map(str, sys.stdin.readline().split()))
    if 'push' in cmd:
        x = int(cmd[1])
        queue.append(x)
    elif 'pop' in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.popleft()
            print(a)
    elif 'size' in cmd:
        print(len(queue))
    elif 'empty' in cmd:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in cmd:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])