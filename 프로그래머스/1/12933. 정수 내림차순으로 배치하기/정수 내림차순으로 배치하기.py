'''
1. 정수 n을 분리
max?
'''
def solution(n):
    answer = 0
    n = str(n)
    n_list = []
    for i in n:
        n_list.append(i)
    n_list = list(map(int, n))
    n_list.sort(reverse=True)
    answer = "".join(map(str, n_list))
    return int(answer)