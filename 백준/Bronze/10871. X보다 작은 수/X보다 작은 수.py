# x보다 작은 수

n, x = map(int, input().split())
line = list(map(int, input().split()))

for i in line:
    if i < x:
        print(i)