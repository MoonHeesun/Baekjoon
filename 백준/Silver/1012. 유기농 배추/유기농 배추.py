import sys
from collections import deque

def bfs(field, visited, x, y):
    queue = deque()
    visited[x][y] = 1
    queue.append([x, y])

    while len(queue) > 0:   # queue에 남아있는 게 없을 때까지 실행
        [x, y] = queue.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0 <= nx < height and 0 <= ny < width:
                if visited[nx][ny] == 0 and field[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])   # queue에 넣기

T = int(input())
for i in range(T):
    cnt = 0
    width, height, loc = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(width)] for _ in range(height)]
    visited = [[0 for _ in range(width)] for _ in range(height)]   # 방문 체크 리스트
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for l in range(loc):
        w, h = map(int, sys.stdin.readline().split())
        field[h][w] = 1 
    for i in range(height):
        for j in range(width):
            if field[i][j] == 1 and visited[i][j] == 0:
                bfs(field, visited, i,j)
                cnt += 1
    print(cnt)