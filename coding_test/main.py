n, c = map(int, input().split())
array = list()
for _ in range(n):
    array.append(int(input()))

# 범위 : 집과 집사이의 거리
left = array[1] - array[0]
right = array[-1] - array[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    value = array[0]
    count = 1

    # 공유기 설치
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        left = mid + 1
        # 가장 인접한 두 공유기 사이의 거리
        result = mid
    else:
        right = mid - 1

print(result)
