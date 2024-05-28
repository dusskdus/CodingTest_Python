from math import prod
def solution(num_list):
    nsum = sum(num_list)
    mul = prod(num_list)
    if mul<nsum*nsum:
        return 1
    else:
        return 0