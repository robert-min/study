def check(alp):
    temp = ord(alp) - 65
    if temp < 14:
        return temp
    else:
        return 26 - temp

def solution(name):
    answer = 0
    # name -> list
    name_lst = list(name)

    # 예외 : 첫번째 오른쪽이 "A"일 경우 리스트 reverse
    first = name_lst[0]
    name_lst = name_lst[1:]

    if name_lst[0] == "A":
        name_lst.reverse()

    # 마지막 자리가 "A"인 경우 확인할 필요가 없음
    while name_lst[-1] == "A":
        name_lst = name_lst[:-1]

    answer += check(first)



    # 모든 자리 확인
    for i in name_lst:
        answer += 1
        if i == "A":
            pass
        else:
            answer += check(i)


    return answer

print(solution("JAN"))