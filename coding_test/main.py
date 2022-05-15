import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# dfs
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True
    ret = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= 10:
            continue
        if visited[nx][ny] or M[x][y] != M[nx][ny]:
            continue
        ret += dfs(nx, ny)
    return ret


def dfs2(x, y, val):
    visited2[x][y] = True
    M[x][y] = "0"
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= 10:
            continue
        if visited2[nx][ny] or M[nx][ny] != val:
            continue
        dfs2(nx, ny, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != "0":
                tmp.append(M[j][i])
        for j in range(N - len(tmp)):
            M[j][i] = "0"
        for j in range(N - len(tmp), N):
            M[j][i] = tmp[j - (N - len(tmp))]


def new_array(N):
    return [[False] * 10 for _ in range(N)]


# 입력
N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
visited = new_array(N)
visited2 = new_array(N)

while True:
    exist = False
    visited = new_array(N)
    visited2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == "0" or visited[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            print(res, M[i][j])
            if res >= K:
                dfs2(i, j, M[i][j])  # 지우기
                exist = True

    if not exist:
        break
    down()

for i in M:
    i = i[:-1]
    print("".join(i))