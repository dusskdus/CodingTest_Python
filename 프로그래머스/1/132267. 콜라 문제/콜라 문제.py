'''
1. 보유중인 빈병이 a개 미만이면 받을 수 없으므로 먼저 n-a
2. n-a를 a로 나누면 받는 콜라병 수 
'''
def solution(a, b, n):
    answer = 0
    while(n>=a):
        rb = n%a
        n = (n//a) * b #마트에서 받은 콜라 수 
        answer += n #마트에서 받은거랑 남은거랑 더하기
        n += rb
        
    return answer