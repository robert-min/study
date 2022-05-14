dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 지점당 꽃심을 때 비용
def count_bill(x, y):
    temp = map_bill[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            pass
        else:
            temp += map_bill[nx][ny]
    bill_result[x][y] = temp
    return temp

# 꽃 심음
def plant(x, y):
    bill_result[x][y] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            pass
        else:
            bill_result[nx][ny] = False

def check(x, y):
    flag = True
    if not bill_result[x][y]:
        flag =  False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            pass
        else:
            if not bill_result[nx][ny]:
                flag = False
    return flag

# 입력
N = int(input())
map_bill = list()
for _ in range(N):
    map_bill.append(list(map(int, input().split())))

bill_result = [[0] * N for i in range(N)]



# 3회 반복(이미 심은 지점 False 처리)
result = 0
for _ in range(3):
    min_value = 201
    min_x, min_y = 0, 0
    # 모든 지점 확인
    for j in range(N):
        for k in range(N):
            value = count_bill(j, k)
            if value < min_value and check(j, k):
                min_value = min(min_value, value)
                min_x, min_y = j, k

    print(min_value)
    # 꽃 심음
    result += min_value
    plant(min_x, min_y)

# 출력
print(result)