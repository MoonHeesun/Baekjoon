N = int(input())
canvas = [[0 for _ in range(100)] for _ in range(100)]

area = 0
for i in range(N):
    X, Y = map(int, input().split())
    for col in range(X, X+10):
        for row in range(Y, Y+10):
            if canvas[row-1][col-1] == 0:
                canvas[row-1][col-1] += 1
                area += 1
            else:
                canvas[row][col] += 0

print(area)