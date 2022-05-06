# 대기실마다 확인하면서 "P"인 곳에서 bfs 호출
# bfs 함수에서 좌표 및 거리를 큐에 넣음
## 거리가 2 미만이고 다음 방문할 곳이 "O"라면 큐에 넣음
## 거리가 2 미만이고 다음 방문할 곳이 "P"라면 False
## 거리가 2면 중지
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(array, x, y):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True
    while q:
        x, y, cost = q.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if array[nx][ny] == "P":
                    return False
                if array[nx][ny] == "O":
                    q.append((nx, ny, cost + 1))
                    visited[nx][ny] = True
    return True

def solution(places):
    answer = []

    for place in places:
        array = [list(place[i]) for i in range(5)]
        flag = True

        for i in range(5):
            for j in range(5):
                if array[i][j] == "P":
                    if not bfs(array, i, j):
                        flag = False
            if not flag:
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

