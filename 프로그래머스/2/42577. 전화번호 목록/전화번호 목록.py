'''
1. 가장 짧은 번호 탐색
2. 해당 번호를 제외하고 다른 번호들과 대조 시작
3. 동일하면 false 출력
'''
def solution(phone_book):
    phone_book.sort()  # 전화번호부를 정렬
    
    for i in range(len(phone_book) - 1):
        # 현재 번호와 다음 번호를 비교하여 접두어 관계인지 확인
        if phone_book[i + 1].startswith(phone_book[i]):
            return False  # 접두어가 발견되면 False 반환
    
    return True  # 접두어가 없으면 True 반환
