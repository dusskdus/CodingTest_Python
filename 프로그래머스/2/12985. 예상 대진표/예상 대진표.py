'''
1. 게임참가자 수 n명, a번째참가자와 b번째 참가자는 몇번째 경기에서 만날까?(만나기 전까지 계속 이김)
2. n명에게 1~n까지 번호부여
3. 
'''

def solution(n,a,b):
    answer = 0
    while a!=b:
        answer+=1
        a,b = (a+1)//2, (b+1)//2

    return answer