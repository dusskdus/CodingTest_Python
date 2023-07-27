'''
1. 맨앞 '{{'와 맨뒤 '}}'를 잘라주고 '},{'을 기준으로 split하면 괄호문자가 모두 사라짐
2. s는 현재 ','를 포함한 문자열 원소 ->[ '1', '1,2', '1,2,3' ]
3. 반복문에 들어오는 원소마다 ','을 기준으로 split ->[ '1, 2' ]가 들어온다면 [ '1', '2' ]
4. answer 배열에 차례대로 append'''
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len) #원소 길이순으로 정렬
    for i in s:
        tuple = i.split(',')
        for j in tuple:
            if int(j) not in answer: #answer에 없으면 삽입
                answer.append(int(j))
    return answer