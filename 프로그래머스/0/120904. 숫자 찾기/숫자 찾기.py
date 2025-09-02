def solution(num, k):
    answer = 1
    for i in str(num):
        if str(k) != i:
            answer += 1
        elif str(k) == i:
            return answer
    if str(k) not in str(num):
        return -1