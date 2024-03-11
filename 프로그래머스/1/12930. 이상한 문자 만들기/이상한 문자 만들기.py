'''
1. 공백 기준으로 쪼개서 리스트에 삽입
2. for문 돌리는데 홀수번째는 소문자로 짝수번째는 대문자로 변경 
'''
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]