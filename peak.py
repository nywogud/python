
with open("ExData/peak.txt", 'r') as f:

    n = int(f.readline())
    x = [list(map(int, f.readline().split())) for _ in range(n)]

    x.insert(0,[0]*(n+2))
    x.append([0]*(n+2))

    for i in range(1, n+1):
        x[i].insert(0, 0)
        x[i].append(0)

    peakNum = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[i][j] > x[i-1][j] and x[i][j] > x[i+1][j] and x[i][j] > x[i][j-1]\
                    and x[i][j] > x[i][j+1]:
                peakNum += 1

    print("봉우리 개수는 {}".format(peakNum))


    # x = list(map(str, f.readline()))
    # # ['27 33 80 73 19 23 15\n', '48 84 61 3 36 9 62\n', '87 57 3 14 69 17 22\n', '17 57 86 21 85 51 82\n',
    #  # '7 94 66 21 19 41 82\n', '27 5 59 28 26 77 64\n', '5 46 4 63 76 99 8']
    #
    #
    # temp = []
    # for i in x:
    #     temp.append(i)
    # print(temp)

    # n = int(f.readline())
    #
    # a = []
    # for i in range(n):
    #     a.append(f.readline().split())
    # print(a)

    # n = int(f.readline())
    # a = [list(map(int, f.readline().split())) for _ in range(n)]
    # a.insert(0, [0]*n)
    # a.append([0]*n)
    #
    # for xx in a:
    #     xx.insert(0,0)
    #     xx.append(0)
    #
    # print(a)
    #
    #
    # cnt = 0
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         if (a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and\
    #                 a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]):
    #             cnt += 1
    #
    # print("봉우리 갯수는 {}개".format(cnt))
