
# import numpy as np
#
# def magicSquare():
#     n = int(input("n*n 마방진을 위한 n값을 입력(3이상, 홀수)"))
#     matrix = np.zeros((n, n), dtype=int)
#
#     s_row=0; s_col=n//2
#     matrix[s_row, s_col] = 1
#
#     row = 0
#     col = 0
#
#     for i in range(2,n*n+1):
#         row = s_row # 전 위치값 row값 보관
#         col = s_col # 전 위치값 col값 보관
#
#         s_row = s_row -1 ; s_col = s_col +1
#
#         if s_row < 0:
#             s_row = n-1
#         if s_col > 0:
#             s_col = 0
#         if matrix[s_row,s_col] ==0:
#             matrix[s_row, s_col] = i
#         else: # 0이 아니면 다른 숫자가 있다는 얘기
#             s_row = row+1; s_col = col
#             matrix[s_row, s_col] = i # IndexError: index 3 is out of bounds for axis 0 with size 3.
#
#     return matrix

def magicSquare():
    n = int(input("n*n의 마방진 숫자 입력(홀수만)..."))

    #3x3 2차원 배열 생성
    arr = [[0]*n for _ in range(n)]

    arr[0][n-2] = 1

    print(arr)

magicSquare()