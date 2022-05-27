from collections import deque
# bfs
def bfs(start, adj, visited):
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for i in adj[cur]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[cur]+1

def solution(n, edge):
    answer = 0

    # 간선 저장
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e[0], e[1]
        adj[a].append(b)
        adj[b].append(a)

    # 1번노드부터 탐색
    # bfs
    visited = [0 for _ in range(n + 1)]
    bfs(1, adj, visited)
    max_e = max(visited)
    for v in visited[2:]:
        if v == max_e:
            answer +=1

    # visited 값이 max인거의 개수가 answer
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))