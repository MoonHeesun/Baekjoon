# 행렬 덧셈
n, m = map(int, input().split())

mat1 = [[0 for _ in range(m)] for _ in range(n)]
mat2 = [[0 for _ in range(m)] for _ in range(n)]
mat3 = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    cols = list(map(int, input().split()))
    for j in range(m):
        mat1[i][j] = cols[j]

for i in range(n):
    cols = list(map(int, input().split()))
    for j in range(m):
        mat2[i][j] = cols[j]

for i in range(n):
    for j in range(m):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
        print(mat3[i][j], end=' ')
    print()