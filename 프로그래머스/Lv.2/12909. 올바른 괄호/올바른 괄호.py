'''
1. 스택으로 생각해보기
2. 일단 맨앞의 문자가 ')'라면 False
3. 맨앞의 문자가 '('이고, 개수가 동일하다면 True
'''
def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()

                
    return len(stack) == 0
