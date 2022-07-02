def solution(lottos, win_nums):
    answer = []
    zero, sum = 0, 0

    # 0 개수 체크
    for num in lottos:
        if num == 0:
            zero += 1
        else:
            if num in win_nums:
                sum += 1

    # 최고 순위

    max_count = 7 - (sum + zero)
    if max_count == 7:
        answer.append(6)
    else:
        answer.append(max_count)

    # 최저 순위
    if sum == 0:
        answer.append(6)
    elif sum == 1 and zero == 0:
        answer.append(6)
    elif sum == 1 and zero != 0:
        answer.append(5)
    else:
        answer.append(7 - sum)

    return answer

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))