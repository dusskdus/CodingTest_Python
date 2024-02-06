'''
문자열 압축
1. 입력받은 s를 for문 돌리면서 탐색 (s의 길이만큼)
2. 최소단위로 쪼개기
3. 중복값을 확인하고 최솟값을 출력!
'''

def solution(s):
    result=[]
    
    if len(s)==1: #문자가 한개라면 1출력
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1 #문자열이 반복되는지 체크
        tmp=s[:i] #문자열이 앞에 문자열과 연속되는지 체크

        for j in range(i, len(s)+i, i):           
            if tmp==s[j:i+j]: 
                cnt+=1
            else:
                if cnt!=1: 
                    b = b + str(cnt)+tmp #반복되는 문자 넣기
                else:
                    b = b + tmp #그냥 문자만
                    
                tmp=s[j:j+i]
                cnt = 1
                
        result.append(len(b))
        

    return min(result) #최소값 출력