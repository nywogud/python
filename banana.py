#banana -> 답 4
#banana1 -> 답 5

#숙성 바나나의 좌표값을 알아내서 queue에 넣기

from collections import deque
Q = deque()
with open("./ExData/banana", 'r') as f:
    y, x = f.readline().split()
    x = int(x)
    y = int(y)
    print("x, y = {}, {} ".format(x, y))
    lst = [list(map(int, f.readline().split())) for _ in range(x)]

for i in lst:
    print(i)
temp = [[0]*y]*x
print()

for i in temp:
    print(i)
print()
for i in lst:
    print(i)
print()

for i in range(x):
    for j in range(y):
        if lst[i][j] == 1:
            Q.append((i, j))
        else:
            continue

print(Q) # 여기서부터 시작한다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while Q:
    temp = Q.popleft()
    for i in range(4):
        nx = temp[0] + dx[i]
        ny = temp[1] + dy[i]
        if <=좌표의 조건을  걸어 <= and lst[nx][ny] == 0:
            lst[nx][ny] =1
        else:
            break

for i in lst:
    print(i)



# while True: #무한루프
#     if level == n//2:
#         break
#     size = len(Q)
#     for i in range(size):
#         temp = Q.popleft()
#         for j in range(4):
#             x=temp[0]+dx[j]
#             y=temp[1]+dy[j]
#             if ck_tbl[x][y]==0:
#                 total += matrix[x][y]
#                 ck_tbl[x][y]= 1
#                 Q.append((x,y))
#                 print("level={} Qsize={}  x={} y={}".format(level, size, x, y))
#                 for xx in ck_tbl:
#                     print(xx)
#                 print()
#     level +=1
#
# print(total)





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