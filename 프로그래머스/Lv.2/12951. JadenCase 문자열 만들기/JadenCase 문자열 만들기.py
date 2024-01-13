'''
1. 공백을 기준으로 문자열을 나누기
2. 첫 문자만 대문자로 변환 -> capitalize 함수 존재
3. 나머지 문자는 소문자로 변환
'''
def solution(s):
    str_list = s.split(' ')
    answer = ''
    for i in range(len(str_list)):
        str_list[i] = str_list[i].capitalize()
    answer=' '.join(str_list)
    return answer
    