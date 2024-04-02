'''
0. name과 yearning을 key:value로 지정
1. 반복문을 돌면서 photo안에 name이 있는지 확인
2. 있는 이름의 yearing만 더해서 result에 삽입
'''

def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    for people in photo:
        score = 0
        for person in people:
            score += info.get(person, 0)
        answer.append(score)
                
    return answer