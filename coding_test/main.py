import copy

N = int(input())
array = list(map(int, input().split()))

# dp[i] : i까지 왔을 때 합이 최대
dp = copy.deepcopy(array)

for i in range(1, N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(array[i] + dp[j], dp[i])

print(max(dp))
