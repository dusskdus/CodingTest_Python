'''
1. 입력값의 합을 곱으로 나태내야함
2. yellow를 brown이 감싸야함
3. yellow를 잘 생각해보면 -> ..몰라
4. h=세로, w=가로, h<=w
5. brown + yellow = h*w
6. (h-2)*(w-2)=yellow
 hw-2h-2w+4=yellow
 hw-2(h+w)+4 = yellow
7. brown = 2(h+w)-4
'''
def solution(brown, yellow):
    answer = []
    h=0
    w=0
    for i in range(1, yellow+1):
        if yellow%i == 0:
            h = (yellow//i)+2
            w = i+2
            if 2*(h+w)-4 == brown:
                answer.append(w)
                answer.append(h)
                #가로가 세로보다 크거나 같아야 하기 때문에 내림차순으로 정렬을 한 리스트가 반환
                return sorted(answer, reverse = True)
    
    return answer