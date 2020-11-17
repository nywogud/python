# def appleTree():

    # xnumber = int(f.readline().replace("\n", ""))
    #
    # print(xnumber)
    #
    # for i in (xnumber +1):


    # text = f.readline()
    # print(text)
    # number = []
    # for i in range(len(text)):
    #     number.append((text[i].replace("\n", "").replace(" ", ",")))
    #
    # print(number)
    #
    # numberList = []
    # for i in range(len(number)):
    #     numberList.append(list(number[i].split()))

    # print(numberList)


################################################################

def appleTree1():
    with open("./ExData/appleTree.txt", "r") as f:

        # 이해 안되도 외우기
        # '_'의 의미 : '_' 써서 인덱스 변수 안 쓰고 n개 만큼 돌리겠다는 의미
        n = int(f.readline())
        a = [list(map(int, f.readline().split())) for _ in range(n)]

        sum = 0
        s = e = n // 2
        for i in range(n):
            for j in range(s, e + 1):
                sum = sum + a[i][j]
            if i < n // 2:
                s = s - 1;
                e = e + 1
            else:
                s = s + 1;
                e = e - 1
        print(sum)

appleTree1()