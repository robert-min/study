from collections import deque

def bfs(begin, target, words, visited):
    queue = deque()
    queue.append((begin, 0))
    while queue:
        cur, depth = queue.popleft()

        if cur == target:
            return depth

        for i in range(len(words)):
            if visited[i] == True:
                continue
            count = 0
            # 단어를 하나씩 뽑아내서 비교
            for a, b in zip(cur, words[i]):
                if a != b:
                    count += 1
            # 단어가 하나가 같은 경우만 계속 탐색(하나만 바꿀 수 있다고 함)
            if count == 1:
                visited[i] = True
                queue.append((words[i], depth + 1))


def solution(begin, target, words):
    answer = 0
    # target이 words에 없는 경우 return 0
    if target not in words:
        return 0
    # 현재 단어와 한글자 차이가 있는 단어 선택해서 저장
    visited = [False] * (len(words))
    answer = bfs(begin, target, words, visited)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))