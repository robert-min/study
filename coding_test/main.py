n = int(input())
array = list()
array.append((0, 0,0, 0))

for i in range(1, n + 1):
    area, height, weight = map(int, input().split())
    array.append((i, area, height, weight))

# 무게 기준으로 정렬
array.sort(key=lambda x : x[3])

# 높이 저장
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])

# 역추적
max_value = max(dp)
index = n
result = list()
while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1

result.reverse()
print(len(result))
[print(i) for i in result]