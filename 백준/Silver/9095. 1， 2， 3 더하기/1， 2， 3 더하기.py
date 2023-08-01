t = int(input())

def fn(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    return fn(num-1)+fn(num-2)+fn(num-3)

for i in range(t):
    n = int(input())
    print(fn(n))