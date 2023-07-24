# 방법 1
def d(n):
    ans = n
    num = list(str(n))
    for i in range(len(num)):
        ans += int(num[i])
    return(ans)

array = list(range(1,10001))

for i in range(1, 10001):
    if d(i) in array:
        array.remove(d(i))

for i in array:
    print(i)


# 방법 2
# array = [i for i in range(1,10001)]

# for start in range(1, 10001):
#     share = start
#     d = 0
#     while share != 0:
#         rest = share%10
#         share = share//10
#         d += rest
#     next = start+d+share
#     if next in array:
#         array.remove(next)
#     else:
#         continue

# for i in array:
#     print(i)
