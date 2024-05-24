def solution(n):
    answer = 0
    if n%2==0: #n이 짝수
        for i in range(n+1):
            if i%2==0:
                answer += i*i
    elif n%2==1:
        for i in range(n+1):
            if i%2==1:
                answer += i
    return answer
            