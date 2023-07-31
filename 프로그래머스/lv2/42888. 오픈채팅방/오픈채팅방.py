def solution(record):
    answer = []
    dic = {}
    for i in record:
        record_split = i.split() #split : 문자열 잘라서 리스트 생성
        if len(record_split) == 3: 
            dic[record_split[1]] = record_split[2] #id와 이름으로 key, value값 지정
    for i in record:
        record_split = i.split() #split : 문자열 잘라서 리스트 생성
        if record_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[record_split[1]])
        elif record_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[record_split[1]])

    return answer


#print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))