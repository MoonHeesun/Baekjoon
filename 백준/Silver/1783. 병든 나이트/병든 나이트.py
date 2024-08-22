N, M = map(int, input().split())

# 이동 횟수 4번보다 적은 경우 -> 이동 방법 제약 X
if N == 1: # 이동 불가
    print(1)
elif N == 2:
    if M <= 2:
        print(1)
    elif M > 2 and M <= 4:
        print(2)
    elif M > 4 and M <= 6:
        print(3)
    else:
        print(4)
elif N >= 3:
    if M <= 3:
        print(M)
    elif M >= 4 and M <= 6:
        print(4)
    elif M >= 7:
        print(M-2)