# def gridSumMax():
with open("./ExData/girdSumMax", 'r') as f:
    a = f.readlines()
    n = len(a)

with open("./ExData/girdSumMax", 'r') as f:
    gridList = []
    for i in range(n):
        gridList.append(list(map(int, f.readline().split())))
    result = 0
    for i in range(n):
        garoSum = seroSum = 0
        for j in range(n):
            garoSum = garoSum + gridList[i][j]
            seroSum = seroSum + gridList[j][i]
            if garoSum > result:
                result = garoSum
            if seroSum > result:
                result = seroSum

    # 이런식으로 대각선도 인덱싱으로 함


# a = int[list(map(int, f.readline().split())) for _ in range(n)]
