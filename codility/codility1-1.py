def solution(A):
   diff = None
   for i in range(1, len(A)):
       first_part = A[0:i]
       second_part = A[i-len(A):]
       if diff == None:
           diff = abs(sum(first_part) - sum(second_part))
       else:
           new_diff = abs(sum(first_part) - sum(second_part))
           if new_diff < diff:
               diff = new_diff
               
   return diff



def solution2(A):
    # write your code in Python 2.7
    head = A[0]
    tail = sum(A[1:])
    min_diff = abs(head-tail)

    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        new_min_diff = abs(head-tail)
        if new_min_diff < min_diff:
            min_diff = new_min_diff
    return min_diff
