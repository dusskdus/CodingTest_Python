def solution(hp):
    answer = 0
    R = 0
    r = 0
    if hp%5==0:
        answer += hp//5
    else:
        answer+= hp//5
        R = hp%5
        if R%3 ==0:
            answer += R//3
        else:
            answer += R//3
            r = R%3
            answer += r
            
        
    return answer