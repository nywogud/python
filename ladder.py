# with open("./ExData/ladder", 'r') as f:
#     x = int(len(f.readlines()))
#
# print(x)
#
# with open("./ExData/ladder", 'r') as f:
#     ladder = [list(map(int, f.readline().split())) for _ in range(x)]
#
# for i in ladder:
#     print(i)
#
# pointer = []
# for i in range(x):
#     for j in range(x):
#         if ladder[i][j] == 2:
#             pointer.append((i,j))
#
# print(pointer)
#
# chktbl = [[0]*x]*x
# for i in chktbl:
#     print(i)
#
# def DFS(x,y):
#     chkTbl[x][y] = 1
#     if ladder[x] == 0:
#         break
#     else:


def DFS(row,col):
    chTbl[row][col] = 1
    if row == 0:
        print("{} : 이 칸에서 출발 ".format(col))
    else:
        # 인덱스 에러 확인, 벽인지 아닌지 확인, 왔던 곳인지 아닌지 체크
        if col-1>=0 and matrix[row][col-1]==1 and chTbl[row][col-1]== 0:
            DFS(row,col-1)
        elif col +1 <10 and matrix[row][col+1]==1 and chTbl[row][col+1]== 0:
            DFS(row, col+1)
        else:
            DFS(row-1, col)

f=open("./ExData/ladder", 'r')
matrix = [list(map(int, f.readline().split())) for _ in range(10)]
chTbl = [[0]*10]*10
for col in range(10):
    if matrix[9][col]==2:
        DFS(9,col)

for i in chTbl:
    print(i)