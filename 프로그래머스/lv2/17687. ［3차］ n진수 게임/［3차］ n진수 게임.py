'''
1. 숫자 n을 base진법으로 만드는 함수를 정의
  1-1. "0123456789ABCDF" 문자열을 생성하고, n 을 base로 나눈 몫과 나머지를 구함
  1-2. 몫이 0이면 문자열의 나머지 인덱스를 리턴
  1-3. 0이 아니라면 convert(몫, base)를 재귀호출하고, 문자열의 나머지 인덱스 붙이기
2. 참가 인원 m x 미리 알 개수 t의 최댓값인 100000까지의 n진법을 구하여 하나의 문자열 test로 구성
3. answer의 길이가 t보다 작으면 반복
  3-1. answer에 test의 튜브순서 p번째 단어를 붙임
  3-2. p에 참가 인원 m을 ㄷㅓㅎㅏㄱㅣ'''
def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base) #몫과 나머지를 튜플형식으로 반환
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
        
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
        
    return answer

#print(solution(2, 4, 2, 1))