'''
딕셔너리로 쌍을 지어서 매핑해둔 다음, 리스트에서 영어가 있다면 변경시키는 방법
'''
def solution(s):
    answer = 0
    dic = {'zero':'0', 'one':'1', 'two':'2','three':'3','four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    if s.isdigit() == False:
        for key, value in dic.items():
            s = s.replace(key, value)
        answer = int(s)
    else:
        answer = int(s)
    return answer