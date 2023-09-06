def solution(survey, choices):
    answer = ''
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    '''for i in choices:
        if i<4:
            for j in survey:
                score[j[0]] += 4-i
        elif i>4:
            for j in survey:
                score[j[1]] += i-4'''
    for i,j in zip(survey, choices) :
        if j < 4 :
            score[i[0]] += (4 - j)
        elif j > 4 :
            score[i[1]] += (j - 4)
    
    test = list(score.items())

    for i in range(0,len(test),2) :
        if test[i+1][1] > test[i][1] :
            answer += test[i+1][0]
        else :
            answer += test[i][0]


    
    return answer