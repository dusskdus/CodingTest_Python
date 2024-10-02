'''
1. n마리의 포켓몬 중 n/2 획득 가능
2. 같은 종류의 포켓몬 = 같은 번호
3. 최대한 다른 종류의 포켓몬을 가질 수 있도록
'''
'''
1. 일단 총 len(nums) 파악, len(nums)/2
2. 중복되는 숫자 제거
3. 제거 후 len(nums)파악하고
4. 만약 len(nums)/2>=len(nums)면 그대로 len(nums)출력

'''
def solution(nums):
    answer = 0
    half = len(nums)//2
    non = list(set(nums))
    if half>=len(non):
        return len(non)
    else:
        return half
        