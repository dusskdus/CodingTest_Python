def solution(a, b):
    answer = 0
    ab = str(a) + str(b)
    if int(ab) > 2*a*b:
        answer = int(ab)
    elif int(ab) < 2*a*b:
        answer = 2*a*b
    elif int(ab) == 2*a*b:
        answer = int(ab)
    return answer