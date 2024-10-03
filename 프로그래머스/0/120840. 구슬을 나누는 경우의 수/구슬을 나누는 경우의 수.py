'''
가진구슬 : balls
나눠줄구슬 : share
가진 구슬이 모두 다르다고 할때 구슬을 나눠줄 수 있는 경우의 수 구하기
'''
import math
def solution(balls, share):
    answer = 0
    answer = math.comb(balls, share)
    return answer