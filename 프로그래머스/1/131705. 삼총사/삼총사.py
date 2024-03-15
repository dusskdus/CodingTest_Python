'''
1. 숫자 3개를 전부 더해서 0이되면 삼총사
2. 0이 되면 +1
3. combination 이용
'''
from itertools import *
def solution(number):
    answer = 0
    printList = list(combinations(number, 3))
    for i in printList:
        if sum(i)==0:
            answer+=1
    return answer