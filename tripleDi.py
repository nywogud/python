with open("./ExData/tripleDi") as f:
    n = int(f.readline())
    num = []
    for i in range(n):
        num.append(list(map(int, f.readline().split())))

moneyList = []
for i in range(n):
    money = 0
    if num[i][0] == num[i][1] == num[i][2]:
        money = 10000 + (num[i][0]*1000)
        moneyList.append(money)

    elif num[i][0] != num[i][1] != num[i][2]:
        num[i].sort(reverse=True)
        money = (num[i][0])*100
        moneyList.append(money)

    else:
        num[i].sort(reverse=True)
        money = 1000 + (num[i][0] *100)
        moneyList.append(money)

moneyList.sort(reverse=True)
print(moneyList[0])

########################################################
#
# with open("./ExData/tripleDi") as f:
#     n = int(f.readline())
#     for i in  range(n):
#         temp = list(map(int, f.readline().split()))
#
#         maxPrize = 0
#         temp.sort()
#         a,b,c = temp
#
#         if a==b and b==c:
#             prize =
#
# ...... 먼저 정렬하고 값에 담아서 값을 비교하는게 더 간단하게 짤 수 있을 것 같음. 눈을 비교하는 문제.