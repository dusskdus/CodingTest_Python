'''
평행하려면? 기울기가 같아야함
기울기를 구하는 공식을 이용한다.
'''

def solution(dots):
    def is_parallel(a, b, c, d):
        # (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)
        return (dots[b][1] - dots[a][1]) * (dots[d][0] - dots[c][0]) == \
               (dots[d][1] - dots[c][1]) * (dots[b][0] - dots[a][0])
    
    # 세 가지 가능한 선분 쌍 조합
    if is_parallel(0, 1, 2, 3):
        return 1
    if is_parallel(0, 2, 1, 3):
        return 1
    if is_parallel(0, 3, 1, 2):
        return 1
    return 0
