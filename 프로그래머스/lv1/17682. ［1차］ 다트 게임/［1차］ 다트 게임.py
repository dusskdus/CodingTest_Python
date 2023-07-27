def solution(dartResult):
    n = ''
    score = []
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i in bonus:
            score.append(int(n) ** bonus[i])
            n = ''
        elif i == '*':
            score[-2:] = [s*2 for s in score[-2:]]
        elif i == '#':
            score[-1] = -score[-1]       

    return sum(score)