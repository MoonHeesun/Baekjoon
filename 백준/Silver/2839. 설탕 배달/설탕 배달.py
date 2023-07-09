N = int(input())

num = []

for i in range(1001):
    for j in range(1667):
        mul = (5*i)+(3*j)
        if mul == N:
            num.append((i+j))

if len(num) > 0:
    print(min(num))
else:
    print(-1)