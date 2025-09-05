# 2단계: 효율성까지 해결하여 최종 완성된 코드
def solution(participant, completion):
    # 1. 두 리스트를 모두 정렬하여 비교 준비 (핵심!)
    participant.sort()
    completion.sort()
    
    # 2. 정렬된 두 리스트를 같은 인덱스끼리 비교
    # (completion 길이가 1 작으므로 그 길이만큼만 비교하면 안전)
    for i in range(len(completion)):
        # 3. 같은 위치(인덱스)의 이름이 다르면, 그 참가자가 완주 못한 사람
        if participant[i] != completion[i]:
            return participant[i]
    
    # 4. 위 반복문을 다 통과했다는 것은, 마지막 주자가 완주하지 못했다는 의미
    return participant[-1]