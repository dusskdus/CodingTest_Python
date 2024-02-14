'''
1. 피보나치 수열을 이용하기 -> 정답에 있어서 그 이전 수열과 이전수열을 더하여 정답을 구함
2. f = (f-1) + (f-2)
'''
def solution(n):
    answer = 0
    a, b = 0,1
    
    for i in range(n) :
        a,b = b, a+b
    
    answer = b % 1234567
    return answer