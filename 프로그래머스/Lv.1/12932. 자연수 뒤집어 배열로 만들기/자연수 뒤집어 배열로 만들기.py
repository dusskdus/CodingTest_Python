'''
1.자연수를 나눠서 리스트 안에 집어넣기
2.sort 함수 사용해서 뒤집기
'''
def solution(n):
    a = []
    s = reversed(str(n))
    for i in s:
        a.append(int(i))
    return a