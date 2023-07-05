# (r, c) = (북,서)
# 윗면 = 1, 동쪽면 = 3  -> (x,y)
# 처음엔 주사위 모두 0
# 칸의 수가 0 이면 맞닿은 주사위 면의 숫자 복사
# 0 아니면 칸에 써있는 수가 주사위로 옮겨감(칸은 0)


# 이동 후 바뀐 주사위 면의 숫자 구하기
def dice_move(dir):
    if dir == 1: # 동
        dice[0], dice[2], dice[5], dice[1] = dice[1], dice[0], dice[2], dice[5]
    elif dir == 2: # 서
        dice[0], dice[1], dice[5], dice[2] = dice[2], dice[0], dice[1], dice[5]
  
    elif dir == 3: # 북
        dice[0], dice[4], dice[5], dice[3] = dice[3], dice[0], dice[4], dice[5]

    elif dir == 4: # 남
        dice[0], dice[3], dice[5], dice[4] = dice[4], dice[0], dice[3], dice[5]


# 지도 크기, 주사위 좌표, 명령의 개수 입력
N, M, x, y, K = map(int, input().split())

# 지도 칸의 수 입력
num = []
for i in range(N):
    num.append(list(map(int, input().split())))

# 이동 명령 입력
move_num = list(map(int, input().split()))

# 주사위가 놓여진 지도 칸에 적힌 수 구하기
dice = [0,0,0,0,0,0]    # [밑, 동, 서, 북, 남, 위]

dx = [0, 0, -1, 1]  # 북(x3), 남(x4) 이동
dy = [1, -1, 0, 0]  # 동(y1), 서(y2) 이동

for i in range(K):
    dir = move_num[i]
    nx = x + dx[dir - 1]
    ny = y + dy[dir - 1]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:  
        continue    # 지도 범위 벗어나면 무시

    dice_move(dir)  # 주사위 이동

    if num[nx][ny] == 0:
        num[nx][ny] = dice[0]
    else:
        dice[0] = num[nx][ny]
        num[nx][ny] = 0

    x = nx
    y = ny

    print(dice[5])  # 주사위 윗면 출력
    
