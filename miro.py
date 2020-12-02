# from collections import deque
# f = open("./ExData/miro", 'r')
# matrix = [list(map(int,f.readline().split())) for _ in range(7)]
# f.close()
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# dis = [[0]*7 for _ in range(7)]
# Q=deque()
# Q.append((0,0))
# matrix[0][0] = 1 # 처음 시작점을 체크한 후 시작
# while Q:
#     print(Q)
#     temp = Q.popleft()
#     for i in range(4): # 위, 아래, 왼쪽, 오른쪽 좌표값 계산
#         x = temp[0] +dx[i]
#         y = temp[1] +dy[i]
#         if 0<=x<=6 and 0<=y <=6 and matrix[x][y] == 0:
#             matrix[x][y] = 8
#             dis[x][y]=dis[temp[0]][temp[1]] + 1
#             Q.append((x,y))
#
# if dis[6][6] == 0:
#     print(-1)
# else:
#     print(dis[6][6])

# for xx in matrix:
#     print(xx)
# #답은 12

###########################################################

# f = open("./ExData/miro2", 'r')
# matrix = [list(map(int,f.readline().split())) for _ in range(7)]
# f.close()



############ 재귀함수 :  stack 구조의 이해 #############

matrix = [[0,0,0],
          [0,1,0],
          [0,0,0]]

#시계 방향으로 탐색한다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]


cnt = 0
def DFS(x,y): # Depth First Search(DFS)
    global cnt
    if x == 2 and y==2:
        cnt +=1
    else:
        for i in range(4): # 리스트의 길이 만큼 반복한다.
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=2 and 0<=yy<=2 and matrix[xx][yy]==0:
                matrix[xx][yy]=8
                DFS(xx,yy)
                matrix[xx][yy] = 0
                printA(matrix)

def printA(matrix):
    for xx in matrix:
        print(xx)
    print()

matrix[0][0] = 8
DFS(0,0)
print(cnt)

