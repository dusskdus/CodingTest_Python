'''
1. 일단 d의 총합을 구함
2. budget보다 d가 작으면 return len(d)
3. 크다면, d.sort()후 반복문 돌리기
4. for i in range하면서 sum에 i 더하기 (sum이 budget보다 작거나 같을때까지만)
5. i더할때마다 answer에 +1하기
'''
"""def solution(d, budget):
    d.sort()
    d_sum = 0
    answer = 0
    if sum(d) <=budget:
        return len(d)
    else :
        for i in range(len(d)):
            while (d_sum<=budget):
                d_sum+=i
                answer+=1
                break
            else:
                answer=answer-1
    return answer"""

def solution(d, budget):
    d.sort()
    d_sum = 0
    answer = 0

    for i in d:
        if d_sum + i <= budget:
            d_sum += i
            answer += 1
        else:
            break

    return answer


