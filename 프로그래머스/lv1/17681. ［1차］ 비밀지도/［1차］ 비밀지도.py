def solution(n, arr1, arr2):
    #입력받은 10진수를 2진수로 변환한 후 arr1과 arr2에 저장된 숫자들을 비교해(?)그다음 0이면 ''출력 1이면 #출력
    arr1_2 = []
    arr2_2 = []
    answer = []
    for i in range(n): #10진수를 2진수로 변경
        arr1_2.append(bin(arr1[i])[2:])
        arr2_2.append(bin(arr2[i])[2:])
        arr1_2[i] = ('0' * (n-len(arr1_2[i]))) + arr1_2[i] #n길이에 맞추기(n길이보다 부족한경우 몇개가 부족한지 구해서 추가)
        arr2_2[i] = ('0' * (n-len(arr2_2[i]))) + arr2_2[i]
        tmp = ''
        for j in range(n):
            if arr1_2[i][j] == '1' or arr2_2[i][j] == '1':
                tmp += '#'
            if arr1_2[i][j] == '0' and arr2_2[i][j] == '0':
                tmp += ' '
        answer.append(tmp)
    return answer