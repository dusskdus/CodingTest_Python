'''
1. 공백을 기준으로 모스 부호를 나누기 -> split사용
2. 해독 딕셔너리에서 모스부호와 일치하는 키값찾기
3. value값 추출 후 answer에 삽입
'''
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z' }
    
    
    answer = ''
    for i in letter.split(' '):
        answer += morse[i]
    return answer