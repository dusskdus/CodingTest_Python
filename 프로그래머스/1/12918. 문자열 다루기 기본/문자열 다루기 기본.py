def solution(s):
    #answer = 0
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if s.isdigit():
                return True
            else:
                return False
    else:
        return False
        