'''
1. 약수값을 반환하는 함수가 있는가? --> 없음
'''
def solution(n):
    sor_list = []
    for i in range(1, n+1):
        if n%i==0:
            sor_list.append(i)
    sum = 0
    for j in sor_list:
        sum+=j
    return sum