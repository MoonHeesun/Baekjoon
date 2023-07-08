N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(0)

for i in range(M):
    I, J, K = map(int, input().split())
    for ball in range(I-1, J):
        basket[ball] = K

for i in basket:
    print(i, end=" ")