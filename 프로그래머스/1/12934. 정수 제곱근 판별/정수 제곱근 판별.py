'''
1. 제곱인지 아닌지 판단? 파이썬에 루트 함수가 있는가?
2. math 메서드 이용
'''
import math

def solution(n):
    x = math.sqrt(float(n))
    if int(x) == x:
        return (x+1)*(x+1)
    else:
        return -1