'''
1. n보다 커야함, 2진수 변환시 1의 갯수가 같음
2. 1의 조건을 만족하는 수 중에서 최소값
3. n보다 큰 숫자들 중에서 반복문 돌리며 탐색 -> 시간 초과 발생
4. 
'''
def solution(n):
    answer = 0
    for i in range(n+1, 1000001):
        if bin(n)[2:].count("1") == bin(i)[2:].count("1"):
            answer = i
            break
    return answer
