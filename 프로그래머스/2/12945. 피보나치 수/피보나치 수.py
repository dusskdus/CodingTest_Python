'''
1. n을 입력받음
2. n-1, n-2를 더함
3. 출력
'''
def solution(n):
    arr = [0,1]
    for i in range(2, n+1):
        arr.append((arr[i-1]+arr[i-2])%1234567)
    return arr[-1]