from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):  # 인접 리스트
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)  # 양방향
    graph[v2].append(v1)

for i in range(1, n+1):
    graph[i].sort() # 작은 수부터 방문해야하니까 오름차순 정렬

# dfs
visited_d = [0 for _ in range(n+1)]
visited_d[v] = 1  # 시작 정점 방문 표시
def dfs(curr):
    print(curr, end=' ')

    for i in graph[curr]:
        if visited_d[i] == 0:
            visited_d[i] = 1
            dfs(i)

#bfs
def bfs(start):
    queue = deque()
    queue.append(start) # 시작 정점 큐에 넣기
    visited_b = [0 for _ in range(n+1)]
    visited_b[start] = 1  # 시작 정점 방문 표시

    while len(queue) > 0:   # 큐가 비면 종료
        curr = queue[0]
        print(curr, end=' ')
        for i in graph[curr]:
            if visited_b[i] == 0:
                queue.append(i)
                visited_b[i] = 1 # 방문 표시
        queue.popleft() # 방문 종료 정점 지우기(선입선출)

dfs(v)
print()
bfs(v)