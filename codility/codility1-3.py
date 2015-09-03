def solution(A):
    # write your code in Python 2.7
    l = len(A)
    exp_sum = (l*(l+1))/2
    act_sum = sum(A)
    diff = act_sum - exp_sum
    for i in range(len(A)):
        if A[i] > len(A):
            op = A[i] - diff
    return op

def solution(A):
    N = len(A) + 1
    sum_N = (N * (N+1)) / 2
    return sum_N - sum(A)