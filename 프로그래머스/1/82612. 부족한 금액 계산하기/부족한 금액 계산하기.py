'''
price : 이용료, money : 내가 가진 돈, count : 이용횟수
price*i한걸 sum에 계속 더하기
i의 길이는 count만큼
sum > money -> sum - money를 리턴
else -> 0 리턴
'''

def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += price*i
    if sum > money:
        return sum - money
    else:
        return 0
