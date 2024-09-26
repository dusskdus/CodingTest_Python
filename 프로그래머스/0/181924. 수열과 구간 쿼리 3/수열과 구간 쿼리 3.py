'''
31204
32104
34102
반복문-> len이용?
'''

def solution(arr, queries):
    answer = []
    arr_2 = []
    arr_2 = arr[:]
    for i in range(len(queries)):
        arr[queries[i][0]]=arr[queries[i][1]]
        arr_2[queries[i][1]]=arr_2[queries[i][0]]
        arr[queries[i][1]]=arr_2[queries[i][1]]
        arr_2 = arr[:]
    return arr