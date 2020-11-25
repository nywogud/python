f = open("./ExData/rotatedLine", 'r')
n = len(f.readlines())
f.close()

matrix = []
f = open("./ExData/rotatedLine", 'r')
for i in range(n):
    matrix.append(list(map(int, f.readline().split())))
f.close()
# matrix =  [[2, 4, 1, 5, 3, 2, 6],
#         [3, 5, 1, 8, 7, 1, 7],
#         [8, 3, 2, 7, 1, 3, 8],
#         [6, 1, 2, 3, 2, 1, 1],
#         [1, 3, 1, 3, 5, 3, 2],
#         [1, 1, 2, 5, 6, 5, 2],
#         [1, 2, 2, 2, 2, 1, 5]]


cnt = 0
for i in range(len(matrix)):
    for j in range(n-4):
        if matrix[i][j] == matrix[i][j+4] and matrix[i][j+1] == matrix[i][j+3]:
            cnt += 1

        if matrix[j][i] == matrix[j+4][i] and matrix[j+1][i] == matrix[j+3][i]:
            cnt += 1


############################################################
# for i in range(3):
#     for j in range(7):
#         temp = matrix[j][i:i+5]
#         if temp == temp[::-1]:
#             cnt +=1
#         for k in range(2): # 열의 회문수 찾기
#             if matrix[i+k][j] != matrix[i+4-k][j]:
#                 break
#         else:
#             cnt += 1
#############################################################

print(cnt)

for i in range(10): # 파이썬에는 for else문이 있음
    if i == 11:
        break
else:
    print("Break 문은 수행되지 않았음")

