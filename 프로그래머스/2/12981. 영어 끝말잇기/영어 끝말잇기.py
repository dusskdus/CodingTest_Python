'''
1. 1~n까지 번호가 붙은 n명의 사람이 끝말잇기
2. 탈락자 번호,본인차례가 몇번째일때 탈락하는지
3. 탈락자가 없다면 [0,0] return
4. 사람수는 2이상 10이하
5. (사람수, 단어배열) 입력받음
-------------------------------------------------
1. 중복확인, 앞단어의 끝글자와 연결되는지 확인 -> 반복문이용
2. 탈락자 번호 -> len%n
3. 몇번째인가? -> len//n
4. 이중for문
'''
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]