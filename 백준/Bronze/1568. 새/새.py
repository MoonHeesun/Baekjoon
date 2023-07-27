n = int(input())
k = 1
sec = 0


while n-k != 0:
    if n-k > 0:
        n -= k
        k += 1
        sec += 1
    elif n-k < 0:
        k = 1
        n -= k
        k += 1
        if n == 0:
            sec += 1
            break
        else:
            sec += 1
            
if n-k == 0:
    sec += 1

print(sec)