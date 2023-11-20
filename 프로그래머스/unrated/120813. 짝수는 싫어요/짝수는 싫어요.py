def solution(n):
    odd = []
    for i in range(n+1):
        if i%2 == 1:
            odd.append(i)
    return odd