# 주사위 방향값 응용, 앞에 인덱스가 범위를 벗어나면 방향 꺾기
# 타겟 좌표 구하기

N = int(input())
num = int(input())

table = [[0 for _ in range(N)] for _ in range(N)]

# 방향 조정 (남 -> 동 -> 북 -> 서)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0
d = 0
value = N**2
a = 0
b = 0

while value > 0:
    table[x][y] = value
    if value == num:
        a = x+1
        b = y+1
    if (0 > x+dx[d]) or (x+dx[d] >= N) or (0 > y+dy[d]) or (y+dy[d] >= N) or (table[x+dx[d]][y+dy[d]] != 0):
        d = (d+1)%4
    x = x + dx[d]
    y = y + dy[d]
    value -= 1

for i in range(N):
    for j in range(N):
        print(table[i][j],end=' ')
    print()
print(a, b)
