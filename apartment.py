with open("./ExData/apartment", 'r') as f:
    n = int(f.readline())
    print(n)
    matrix = [list(map(int, f.readline().split())) for _ in range(n)]
    for i in matrix:
        print(i)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(row,col):
    global hCnt
    hCnt +=1
    matrix[row][col] = 8
    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]
        if 0<= nrow < n and 0<= ncol < n and matrix[nrow][ncol] ==1:
            DFS(nrow, ncol)



danji=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            hCnt = 0
            DFS(i,j)
            danji.append(hCnt)

print(danji)
danji.sort(reverse=True)
print("단지수 : {}".format(len(danji)))
for i in danji:
    print(i)