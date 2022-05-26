def solution(answers):
    first_count, second_count, third_count = 0, 0, 0
    # 수포자 답 10000개 이상
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 문제 수 체크
    for idx, ans in enumerate(answers):
        if ans == first[idx % 5]:
            first_count += 1
        if ans == second[idx % 8]:
            second_count += 1
        if ans == third[idx % 10]:
            third_count += 1

    count_dict = {1: first_count, 2:second_count, 3:third_count}

    max_score = max(count_dict.values())
    result = [idx for idx, v in count_dict.items() if v == max_score]

    # # 중복 없는 경우
    # if len(set(count)) == len(count):
    #     result.append(count.index(max(count)))
    # # 중복 있는 경우
    # else:
    #     temp = max(count)
    #     for idx, i in enumerate(count):
    #         if i == temp:
    #             result.append(idx + 1)

    # 최대 값 출력
    return result

print(solution([1,3,2,4,2]))