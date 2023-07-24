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
