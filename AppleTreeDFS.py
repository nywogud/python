# DFS 방식

from collections import deque

f= open("./ExData/appleTree.txt", 'r')
dx=[-1,0,1,0] #시계방향으로 돌아감
dy=[0,1,0,-1] #시계방향으로 돌아감
n=int(f.readline())
matrix = [list(map(int, f.readline().split())) for _ in range(n)]
print(matrix)

level = 0
total = 0 #초기화
Q = deque()
print(Q)

ck_tbl=[[0]*n for _ in range(n)]

for xx in matrix:
    print(xx)
for xx in ck_tbl:
    print(xx)
print()
total +=matrix[n//2][n//2] #중앙값
ck_tbl[n//2][n//2]=1
Q.append((n//2, n//2))

while True: #무한루프
    if level == n//2:
        break
    size = len(Q)
    for i in range(size):
        temp = Q.popleft()
        for j in range(4):
            x=temp[0]+dx[j]
            y=temp[1]+dy[j]
            if ck_tbl[x][y]==0:
                total += matrix[x][y]
                ck_tbl[x][y]= 1
                Q.append((x,y))
                print("level={} Qsize={}  x={} y={}".format(level, size, x, y))
                for xx in ck_tbl:
                    print(xx)
                print()
    level +=1

print(total)

