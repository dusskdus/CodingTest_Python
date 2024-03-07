def solution(elements):
    answer = []
    cycle=elements+elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(cycle[i:i+j]))
    return len(set(answer)) #set은 중복을 제거하는 함수