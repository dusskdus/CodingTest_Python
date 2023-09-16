'''
1. 입력받은 문자열을 리스트에 넣고, 하나씩 탐색
2. i와 i+1이 같다면..pop
3. 처음부터 다시탐색
4. 리스트의 길이가 0이라면 1을 반환
5. 
'''

def solution(s):
    answer = 0
    s = list(s)
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
 
    if len(stack) == 0:
        answer = 1
 
    return answer