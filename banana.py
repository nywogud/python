#banana -> 답 4
#banana1 -> 답 5

#숙성 바나나의 좌표값을 알아내서 queue에 넣기

from collections import deque

f = open("./ExData/banana1", 'r')
col, row = map(int, f.readline().split())
print(col)
print(row)
lst = [list(map(int, f.readline().split())) for _ in range(row)]
for i in lst:
    print(i)
Q = deque()
print(Q)
print(bool(Q))
def serach():
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 1:
                Q.append((i, j))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1
print(bool(Q))
serach()
while Q:
    global cnt
    temp = []
    temp.append(Q.popleft())
    print(Q)
    print(temp)
    for i in range(4):
        nrow = temp[0][0]+ dx[i]
        ncol = temp[0][1]+ dy[i]
        if 0<=nrow<row and 0<=ncol<col and lst[nrow][ncol] == 0:
            lst[nrow][ncol] = 1

    print(Q)
    print(bool(Q))
    if bool(Q)==False:
        cnt +=1
        serach()

    for i in lst:
        print(i)

    pointer = 0
    for i in lst:
        if 0 not in i:
            pointer +=1

    if pointer==row:
        break



print(bool(Q))
print("모든 바나나가 익는데 걸리는 일수는 {}".format(cnt))
for i in lst:
    print(i)






# Q = deque()
# list = [[-1,0,-1], [0,1,0], [-1,0,-1]]
# temp = []
# for i in list:
#     print(i)
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i][j]==1:
#             Q.append((i, j))
#
# print(Q)
#
# from collections import deque
# Q = deque()
# with open("./ExData/banana", 'r') as f:
#     y, x = f.readline().split()
#     x = int(x)
#     y = int(y)
#     print("x, y = {}, {} ".format(x, y))
#     lst = [list(map(int, f.readline().split())) for _ in range(x)]
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
#
# chk_tbl = [[0]*x]*y
# for i in range(x):
#     for j in range(y):
#         if lst[i][j]==1:
#             Q.append((i,j))
# print(Q)
#
# while Q:
#     low,col = Q.popleft()
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         #