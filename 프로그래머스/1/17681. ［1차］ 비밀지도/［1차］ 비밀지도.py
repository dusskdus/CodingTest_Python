'''
1. 각 숫자를 이진수로 변환
2. arr1과 arr2를 비교하면서 or연산
3. 1인건 #으로 변경, 0은 공백으로 변경하기
'''
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 이진수로 변환하고 zfill로 앞자리 0을 채워 길이를 n으로 맞춤
        map1 = bin(arr1[i])[2:].zfill(n)
        map2 = bin(arr2[i])[2:].zfill(n)

        # 두 지도 겹쳐서 벽이 있으면 '#' 없으면 ' '
        line = ''
        for j in range(n):
            if map1[j] == '1' or map2[j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)

    return answer
