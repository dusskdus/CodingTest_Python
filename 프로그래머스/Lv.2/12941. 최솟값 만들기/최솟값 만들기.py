'''
1. 최소값이 되게 하는 방법은? -> 오름차순 정렬, 내림차순 정렬
2. 곱하기
3. 더하기

'''
def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer