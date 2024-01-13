'''
실행한 결괏값 [0,2,4,6,8]이 기댓값 [2,4,6,8,10]과 다릅니다.
i*x
'''
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer