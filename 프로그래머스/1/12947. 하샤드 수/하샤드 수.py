def solution(x):
    arr = list(str(x))
    nsum = 0
    
    for i in range(len(arr)):
        nsum += int(arr[i])
        if x % nsum == 0:
            answer = True
        else:
            answer = False    
    
    return answer