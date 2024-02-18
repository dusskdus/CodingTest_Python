'''
1. 수확한 귤 중에서 k개를 골라 상자 1개에 담아 판매
2. 탠저린 = 귤의 크기를 담은 배열
3. 탠저린에서 min과 max를 구하기 -> 실패
4. 딕셔너리를 생성해서 type과 num을 묶기
'''
def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    for i in dic:
         if k<=0:
            return answer
         k-=dic[i]
         answer+=1
    return answer