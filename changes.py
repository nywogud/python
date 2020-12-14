# 5
# 1 8 20 25 50
# 129

with open("./ExData/changes", 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    k = int(f.readline())

def DFS(coinCnt, sum):
    global finalCnt
    if coinCnt >= finalCnt or sum > k:
        return
    if sum == k:
        if coinCnt < finalCnt:
            finalCnt = coinCnt
    else:
        for i in range(n):
            DFS(coinCnt+1, sum+arr[i])


finalCnt = 9999999999999999
DFS(0,0) # 앞 파람은 동전 갯수, 뒤 파람은 동전의 합
print(finalCnt)


