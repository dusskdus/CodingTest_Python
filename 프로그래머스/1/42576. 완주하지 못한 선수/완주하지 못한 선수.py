'''
한명을 제외하고는 모두가 마라톤을 완주함
마라톤에 참여한 선수들의 이름 배열 -> participant
완주한 선수들의 이름이 담긴 배열 -> completion
완주하지 못한 선수의 이름을 return
동명이인을 어떻게 처리할지가 관건
해시 사용, sort 함수 사용함수 사용
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[len(participant)-1]