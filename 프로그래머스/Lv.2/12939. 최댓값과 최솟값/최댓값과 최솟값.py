'''
1. 문자열을 숫자로 바꾼다 -> 공백을 기준으로 문자열을 나누어서 먼저 리스트에 삽입
2. 최소 최대값을 찾는다 (max, min 함수)
'''
def solution(s):
    strarr = s.split(' ')
    arr = list(map(int, strarr))
    maxnum = max(arr)
    minnum = min(arr)
    return str(minnum)+" "+str(maxnum)