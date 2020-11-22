# def gridSumMax():
with open("./ExData/girdSumMax", 'r') as f:
    a = f.readlines()
    n = len(a)

with open("./ExData/girdSumMax", 'r') as f:
    gridList = [list(map(int, f.readline().split())) for _ in range(n)]

    maxSum = 0

    # 가로,세로 합
    for i in range(len(gridList)):
        x = y = 0
        for j in range(len(gridList)):
            x += gridList[i][j]
            y += gridList[j][i]
            if x > maxSum:
                maxSum = x
            if y > maxSum:
                maxSum = y

    z = 0
    q = 0
    for i in range(len(gridList)):
        z += gridList[i][i]
        q += gridList[i][(n-1)-i]
        if z > maxSum:
            maxSum = z
        if q > maxSum:
            maxSum = q
    print("가로, 세로, 대각선의 합 중 가장 큰 수는  : {}".format(maxSum))

    # gridList = []
    # for i in range(n):
    #     gridList.append(list(map(int, f.readline().split())))
    # result = 0
    # for i in range(n):
    #     garoSum = seroSum = 0
    #     for j in range(n):
    #         garoSum = garoSum + gridList[i][j]
    #         seroSum = seroSum + gridList[j][i]
    #         if garoSum > result:
    #             result = garoSum
    #         if seroSum > result:
    #             result = seroSum