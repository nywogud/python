a = ["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]
orders = []

for i in a:
    orders.append(i.split())
print(orders)
names = []
for i in range(len(orders)):
    names.append(orders[i][0])
print(names)

names = sorted(set(names))
print(names)

orderPerson = []
orderList = []
order = []
for name in names:
    orderList = []
    for i in orders:
        order = i
        if name == order[0]:
            for k in range(1, len(order)):
                orderList.append(order[k])

    orderPerson.append((name, len(set(orderList))))

orderPerson.sort(key=lambda x:(x[1], x[0]), reverse=True)
print(orderPerson)

top = 0
for i in orderPerson:
    if i[1] >= top:
        print(i[0])
        top = i[1]











#################################################################################
#전통적 로직

# orders = ["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]
# names = []
# for xx in orders:
#     nameOder = xx.split()
#     names.append(nameOder[0])
# print(list(set(names)))
#
# nameMenuCnt = []
# for name in names:
#     orderList=[]
#     for xx in orders:
#         order = xx.split()
#         if name == order[0]:
#             for k in range(1, len(order)):
#                 orderList.append(order[k])
#             print(name, orderList)
#     nameMenuCnt.append((name, len(set(orderList))))
#
# nameMenuCnt = list(set(nameMenuCnt))
#
# print(nameMenuCnt)
#
# nameMenuCnt.sort(key=lambda x : (x[1], x[0]), reverse=True)
#
# print(nameMenuCnt)
#
# top = 0
# for xx in nameMenuCnt:
#     if xx[1] >= top:
#         print(xx[0])
#         top = xx[1]

#################################################################################
#python style
# orders = ["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]
#
# testerDic = {}
# for i in orders:
#     i = i.split()
#     if i[0] not in testerDic:
#         testerDic[i[0]] = set(i[1::])
#     else:
#         testerDic[i[0]].update(i[1::])
#     print(testerDic)
#
# for j in testerDic:
#     testerDic[j]=len(testerDic[j])
# print(testerDic)
#
# nameMenuCnt = []
# for key, value in testerDic.items():
#     nameMenuCnt.append((key, value))
# print(nameMenuCnt)
# nameMenuCnt.sort(key=lambda x:(x[1], x[0]), reverse=True)
# print(nameMenuCnt)
# print(nameMenuCnt)
#
# top = 0
# for xx in nameMenuCnt:
#     if xx[1] >= top:
#         print(xx[0])
#         top = xx[1]