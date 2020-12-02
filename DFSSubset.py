# DSF로 부분집합 구하기
def DSF(idx):
    if idx == n+1:
        for i in range(1, n+1):
            if ckTbl[i] ==1:
                print(i, end=' ')
        print()

    else:
        ckTbl[idx] =1
        DSF(idx+1)
        ckTbl[idx] = 0
        DSF(idx+1)

n = int(input("부분집합을 구할 자연수 입력...."))
ckTbl= [0]*(n+1)
DSF(1)




