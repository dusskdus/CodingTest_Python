def solution(id_list, report, k):
    answer = []
    id_d = {}
    r_d = {}
    for i in id_list:
        id_d[i] = set()                 #중복 제거를 위해 set

    for i in set(report):            
        a, b = i.split()
        if a in id_d:
            id_d[a].add(b)              #신고자 d에 신고 받은 자를 추가
        if b in r_d:                   #r에 신고 당한 횟수 누적
            r_d[b] += 1
        else:
            r_d[b] = 1
    
    for j in id_d.values():            #신고 당한 사람들 중지 횟수를 확인해서 카운트
        cnt = 0    
        if len(j) > 0:
            for i in j:
                if r_d[i] >= k:
                    cnt += 1
            answer.append(cnt)
        else:
            answer.append(cnt)
    return answer