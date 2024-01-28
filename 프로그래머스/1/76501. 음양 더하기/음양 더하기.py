'''
1. 정수들의 절댓값을 담은 배열 absolutes
2. 이 정수들의 부호를 차례로 담은 배열 signs
3. 실제 정수들의 합을 구하기
4. signs가 true = +. false = -
5. for문을 이용해서 각 배열을 매치하기
6. 새로운 배열에 집어넣기
'''
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:    #양수라면
            absolutes[i] = +absolutes[i]
        elif signs[i] == False:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)
