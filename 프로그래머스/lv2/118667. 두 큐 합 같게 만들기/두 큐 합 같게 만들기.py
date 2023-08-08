'''
<각 큐의 원소 합을 같게 만들어야함, 만약 불가능 하다면  -1을 반환>
1. queue의 길이만큼 반복문 돌리기며 합 구하기(queue1과 2전부)
2. 
'''
from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    if total%2 == 1:
        return -1
    for i in range(300000):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else: # q2_sum이 q1_sum보다 클 때
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
    return -1