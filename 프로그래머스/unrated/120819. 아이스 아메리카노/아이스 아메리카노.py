'''
1. 배열에 넣는거 : append
'''
def solution(money):
    answer = []
    jan = 0
    rest = 0
    if money%5500==0:
        jan = money//5500
        rest = 0
    else:
        jan = money//5500
        rest = money%5500
    answer.append(jan)
    answer.append(rest)
    return answer