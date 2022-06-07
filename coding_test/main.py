from collections import defaultdict

def solution(genres, plays):
    answer = []
    new_lst = defaultdict(list)
    ord_lst = defaultdict(int)
    idx = 0

    # 장르별로 재생횟수 합 기준으로 정리
    for g, p in zip(genres, plays):
        new_lst[g].append((p, idx))
        ord_lst[g] += p
        idx += 1

    order = sorted(ord_lst.keys(), reverse=True)

    # 장르 내에서 가장 많이 재생한 노래 저장
    for o in order:
        temp = sorted(new_lst[o], key=lambda x: x[0], reverse=True)
        count = 0
        for i in temp:
            answer.append(i[1])
            count += 1
            if count == 2: break

    # 재생횟수가 같을 때 고유번호가 낮은 값

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))