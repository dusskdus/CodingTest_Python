def solution(n):
    answer = 0
    n = str(n)
    str_list = list(n)
    for i in range(len(str_list)):
        answer += int(str_list[i])
    return  answer