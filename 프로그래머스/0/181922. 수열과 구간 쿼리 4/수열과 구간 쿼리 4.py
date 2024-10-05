'''
0은 0을 제외한 모든 수의 배수
query마다 순서대로 s와 e사이에 있는 모든 i에 대해 k의 배수면 arr[i]에 1을 더함
1. 조건 충족 [1, 2, 3, 5, 4]
2. 0~3사이에 있는 2의 배수? [o, x, o, x] -> [2, 2, 4, 5, 4]
3. 0~3사이에 있는 3의 배수? [o, x, x, o] -> [3, 2, 4, 6, 4]
'''
def solution(arr, queries):
    answer = []
    for query in queries:
        for num in range(query[0], query[1]+1): #query[0]부터 query[1]+1사이 값이 num값이 됨
            if num%query[2]==0: #num(실은 i)가 query[2](실은 k)로 나누어 떨어지면(배수면)
                arr[num]=arr[num]+1 #1더하기
            
    return arr