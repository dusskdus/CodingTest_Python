def solution(babbling):
    answer = 0
    niece = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for j in niece:
            i = i.replace(j, ' ')
        i = i.replace(" ", "")  # 공백 제거
        if i == "":
            answer += 1

    return answer
