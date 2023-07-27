
'''뉴스 클러스터링
자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 
두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 
두 집합의 합집합 크기로 나눈 값으로 정의된다.
자카드 유사도 = (교집합크기/합집합크기), 공집합일 경우는 1로 정의
1. str1과 str2를 전부 소문자로 변경
2. 공백 숫자 특수문자가 들어오면 버림(문자쌍을 버리기)
3. 리스트 두개 생성(교집합, 합집합)
4. str1과 str2를 비교하여 겹치는게 있으면 교집합리스트에, 전체는 합집합 리스트에 삽입
5. 자카드 유사도를 answer에 대입하기, 만약 0이라면 1출력하기
'''
def solution(str1, str2):
    answer = 0
    result1 = [] 
    result2 = [] 
    cnt1 = 0
    cnt2 = 0
    #대문자를 소문자로 변경
    str1 = str1.lower()
    str2 = str2.lower()
    if str1==str2:
        return 65536
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): #문자가 아니라면 버리기
            result1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            result2.append(str2[i:i+2])
    for i in result1:
        if i in result2:
            result2.remove(i)
            cnt1+=1
    cnt2=len(result1+result2)

    return int((cnt1/cnt2)*65536) #출력형식 고려