def solution(my_string):
    number = []
    for i in my_string:
        if i.isdigit():
            number.append(int(i))
            
    return sum(number)