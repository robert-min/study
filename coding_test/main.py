import heapq
def dijkstra(start):
    heap_data = list()
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distances[now] < dist:
            continue

        for i in adj[now]:
            cost = dist + i[1]
            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))

for _ in range(int(input())):
    n, d, start = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    distances = [1e9] * (n + 1)

    for _ in range(d):
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))

    dijkstra(start)

    # 출력
    count = 0
    max_distance = 0
    for i in distances:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i

    print(count, max_distance)