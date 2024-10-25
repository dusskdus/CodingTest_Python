def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        days = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            days += 1
        queue.append(days)

    while queue:
        count = 1
        target = queue.pop(0)
        while queue and queue[0] <= target:
            count += 1
            queue.pop(0)
        answer.append(count)

    return answer
