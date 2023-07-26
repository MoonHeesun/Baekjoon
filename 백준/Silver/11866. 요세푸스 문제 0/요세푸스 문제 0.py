from collections import deque

n, k = map(int, input().split())
people = deque([i+1 for i in range(n)])
permu = []
a = 1

while len(permu) != n:
        if a != k:
            people.append(people[0])
            people.popleft()
            a += 1
        else:
            permu.append(people[0])
            people.popleft()
            a = 1
            
print('<', end="")
print(*permu, sep=", ", end="")
print('>')