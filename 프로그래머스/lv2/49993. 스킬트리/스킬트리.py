'''
1. skill_trees 반복문 돌면서 탐색(맨 앞부터 순서확인)
2. 이중 for문 사용하여 만약 skill에 있는 알파벳이 skill_Tree에 존재한다면 스택에 push 하기
3. 하나의 루프 돌때 동일하면 1더하기
'''
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        queue = deque(skill)
        whether = True
        
        for s in tree:
            if s not in queue:
                continue
            else:
                if s == queue[0]:
                    queue.popleft()
                else:
                    whether = False
                    break
        if whether:
            answer += 1
            
    return answer