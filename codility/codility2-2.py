def solution(A):
    # write your code in Python 2.7
    counter = [0]*len(A)
    for element in A:
        if not 1 <= element <= len(A):
            return 0
        if counter[element-1] != 0:
            return 0
        else:
            counter[element-1] = 1
    
    return 1