n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

a = 0
for i in range(n):
    if n_list[i] == v:
        a += 1
print(a)
