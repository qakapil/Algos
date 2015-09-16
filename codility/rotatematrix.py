def solution(A):
    print A
    b = [[False]*3]*3
    t = len(A)
    for i in range(t):
        for j in range(t):
            b[i][j] = A[t-j-1][i]
    print b







A = [[1,2,3],
     [4,5,6],
     [7,8,9],
    ]

solution(A)