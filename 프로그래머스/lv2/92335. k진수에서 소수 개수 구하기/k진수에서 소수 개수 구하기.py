'''
1. n을 k진수로 바꾸기
2. 바꾼 숫자 중에서 0을 기준으로 소수 찾기(1은 소수가 아님(?))
3. 소수의 개수 구해서 답을 출력
1) n을 k진수로 변경
2) 0을 기준으로 split한다음 소수를 판별하여 소수이면 result에 대입
3) list길이를 출력 = 답
진수 변환 함수와 소수판별 함수를 별개로 작성..?
'''
import string
import math
def convert(num, base):
    number = string.digits + string.ascii_uppercase #10진수 출력+영어 대문자 출력
    q, r = divmod(num, base)
    return convert(q, base) + number[r] if q else number[r]

def Prime(n):
    if n == 1:
            return False
    for i in range(2, int(math.sqrt(n)) + 1): #정수의 제곱근 리턴
        if n%i == 0:
            return False
    return True
    
def solution(n, k):
    num = []
    answer = 0
    num = convert(n,k)
    num = num.split("0")
    for i in num:
        if i != "":
            if Prime(int(i)):
                answer += 1
    return answer