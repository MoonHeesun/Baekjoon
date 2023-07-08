# 블랙잭 시간복잡도 줄이기
N, M = map(int, input().split())
card_num = list(map(int, input().split()))

a = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if M < (card_num[i]+card_num[j]+card_num[k]) :
                continue
            else:
                a = max(a, card_num[i]+card_num[j]+card_num[k])

print(a)   