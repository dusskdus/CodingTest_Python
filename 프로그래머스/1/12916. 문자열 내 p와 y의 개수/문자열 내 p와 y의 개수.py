'''
1. 소문자로 변환
2. 반복문으로 p개수 세서 저장
3. y개수 세서 저장
'''
def solution(s):
    answer = True
    
    s = s.lower()
    
    p = s.count('p')
    y = s.count('y')
    
    if(p != y):
        answer = False

    return answer