N, M = map(int, input().split())

basket = []
for i in range(N):
    basket.append(i+1)

for i in range(M):
    I, J = map(int, input().split())
    basket[I-1], basket[J-1] = basket[J-1], basket[I-1]
for i in basket:
    print(i, end=" ")