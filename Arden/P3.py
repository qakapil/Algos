"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of numbers which has the largest sum.

"""

def solution(A):
    max_so_far = max_ending_here = 0
    start = end = None
    for i in range(len(A)):
        max_ending_here = max_ending_here+A[i]

        if max_ending_here < 0:
            max_ending_here = 0
            if i < len(A)-1:
                start = i

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            end = i
    return max_so_far, (start+1, end), A[start+1:end+1]


A = [-2, -3, -4, -1, -2, 1, 5, -10]
print solution(A)
