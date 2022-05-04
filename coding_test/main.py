import math
import sys
input = sys.stdin.readline

def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a * a) + (b * b))

def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

parent = dict()
edges, locations = list(), list()

n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

length = len(locations)

# 각 신과의 거리 그래프 만들기
for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

# 부모 초기화
for i in range(1, n + 1):
    parent[i] = i

# 이미 연결된 신
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# edges 정렬
edges.sort(key=lambda data: data[2])

# 결과 출력
result = 0
for a, b, cost in edges:
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print("%0.2f" % result)