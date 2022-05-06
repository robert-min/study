from collections import deque
# 노드 생성
class Node:
    def __init__(self):
        self.prev = -1
        self.next = -1
        self.is_delete = False  # 삭제 여부 판단

def solution(n, k, cmd):
    # 링크드 리스트 초기화
    node_list = [Node() for _ in range(n)]
    for i in range(n - 1):
        node_list[i].next = i + 1
        node_list[i + 1].prev = i

    # 삭제된 노드 저장할 스택
    del_stack = deque()

    # 명령어 처리
    cur = k
    for c in cmd:
        if len(c) > 1:
            c, move_size = c.split(" ")
            move_size = int(move_size)

        # U
        if c == "U":
            for i in range(move_size):
                cur = node_list[cur].prev

        # D
        if c == "D":
            for i in range(move_size):
                cur = node_list[cur].next

        # C
        if c == "C":
            node_list[cur].is_delete = True
            del_stack.append(cur)
            prev_node = node_list[cur].prev
            next_node = node_list[cur].next

            if prev_node != -1:
                node_list[prev_node].next = next_node
            if next_node != -1:
                node_list[next_node].prev = prev_node
            else:
                cur = prev_node

        # Z
        if c == "Z":
            del_node = del_stack.pop()
            node_list[del_node].is_delete = False
            prev_node = node_list[del_node].prev
            next_node = node_list[del_node].next

            if prev_node != -1:
                node_list[prev_node].next = del_node
            if next_node != -1:
                node_list[next_node].prev = del_node

    # 출력
    answer = ''
    for i in range(n):
        if node_list[i].is_delete:
            answer = answer + "X"
        else:
            answer = answer + "O"
    return answer
