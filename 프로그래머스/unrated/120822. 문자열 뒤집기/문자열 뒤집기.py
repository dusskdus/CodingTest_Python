def solution(my_string):
    answer = ''
    string_list = []
    for i in my_string:
        string_list.append(i)
    string_list.reverse()
    answer = ''.join(string_list)
    return answer