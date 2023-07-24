import sys

n = int(sys.stdin.readline())

a=0
b=1
res=1

for i in range(n-1):
    res = b + a
    a = b
    b = res
print(res)