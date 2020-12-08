# n, m = map(int, input("n과 m을 콤마로 구분해서 입력").split(','))
n, m = 3,2

def DFS(level):
    global cnt
    if level == m :
        for i in range(m):
            print(disp[i], end=' ')
        print()
        cnt +=1
    else:
        for i in range(1,n+1):
            if chkTbl[i] == 0:
                chkTbl[i] = 1
                disp[level] = i
                DFS(level+1)
                chkTbl[i] = 0

disp = [0]*n
chkTbl = [0]*(n+1)
cnt = 0
DFS(0)
print(cnt)
