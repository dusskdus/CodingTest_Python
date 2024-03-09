'''
1. if discount 항목 안에 want가 있는지 확인
2. else면 return 0
3. 있다면 비교 시작
-------------실패---------------
0. counter 모듈 사용 
1. discount 10개씩 묶어서 리스트 생성
2. want와 number, key-value로 묶어서
3. counter 적용한 discount와 동일하다면 answer+=1
4. 출력
'''
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for k in range(len(want)): #want와 number key로 묶기
        dic[want[k]] = number[k]
        
    for i in range(len(discount)-9):
        shop = discount[i:i+10]
        if Counter(shop) == dic:
            answer+=1
    return answer