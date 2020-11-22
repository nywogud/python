def appleTree():

    with open("./ExData/appleTree.txt", 'r') as f:
        n = int(f.readline())
        tangleList =[list(map(int, f.readline().split())) for _ in range(n)]
        print(tangleList)




################################################################

# def appleTree1():
#     with open("./ExData/appleTree.txt", "r") as f:
#
#         # 이해 안되도 외우기
#         # '_'의 의미 : '_' 써서 인덱스 변수 안 쓰고 n개 만큼 돌리겠다는 의미
#         n = int(f.readline())
#         a = [list(map(int, f.readline().split())) for _ in range(n)]
#
#         sum = 0
#         s = e = n // 2
#         for i in range(n):
#             for j in range(s, e + 1):
#                 sum = sum + a[i][j]
#             if i < n // 2:
#                 s = s - 1;
#                 e = e + 1
#             else:
#                 s = s + 1;
#                 e = e - 1
#         print(sum)

appleTree()