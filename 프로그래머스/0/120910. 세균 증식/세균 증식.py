'''
2 4 8 16 32 64 128 256 512 1024 2048
7 14 28 56 112 224 
'''

def solution(n, t):
    answer = n
    for i in range(t):
        answer *= 2
    return answer