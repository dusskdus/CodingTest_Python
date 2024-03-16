'''
1. 인용횟수 중에서 가장 큰 횟수 추출
2. 반복횟수 지정
3. cnt만들어서 +1하기
4. cnt와 i가 같으면 cnt return 하기
'''
def solution(citations):
    cnt = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
            if citations[i] <= i:
                return i
    return len(citations)