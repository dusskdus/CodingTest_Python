'''
모르겟다..ㅇ몰그셋다...
1. 건전지 사용량 = 점프한 거리
2. 순간이동한 거리는 건전지 사용량 0
3. 점프한 거리 = (현재까지 온 거리)*2
4. 건전지 사용량을 출력해야함
5. 무조건 한칸은 이동해야함 -> 1
6. 1*2 만큼 이동 -> 건전지 사용량 1
7. n-2 : 남은 이동거리
8. ...하...
9. 2로 나뉘는지 안나뉘는지 판단해서 2로 나뉘지 않는다면 점프가 필요한거니까 ans+=1
10. n이 0이 될때까지 나누면서 ans를 출력
'''
def solution(n):
    ans = 0
    while n!=0:
        if n%2==0:
            n = n//2
        else:
            ans+=1
            n = n-1

    return ans