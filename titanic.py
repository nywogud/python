# f = open("./ExData/titanic")
# n, m = map(int,f.readline().split())
# lst = list(map(int,f.readline().split()))
# f.close()
#
# boatNum = 0
#
# lst = sorted(lst) # [50, 60, 70, 90, 100]
#
# while lst:
#     lst.pop(0)
#     lst.pop(-1)
#     boatNum += 1

##############################################

# with open("./ExData/titanic", 'r') as f:
#     n, weightMax = map(int,f.readline().split())
#     boatPeople = list(map(int,f.readline().split()))
#
# boatPeople.sort()
# count = 0
#
# while boatPeople:
#     if len(boatPeople) ==1:
#         count +=1
#         boatPeople.pop()
#         break
#     if boatPeople[0] + boatPeople[-1] <= weightMax:
#         boatPeople.pop(-1)
#         count += 1
#     else:
#         boatPeople.pop(0)
#         boatPeople.pop(-1)
#         count += 1
#
# print("필요한 최소의 보트는 {}개.".format(count))

######################################################

from collections import deque
with open("./ExData/titanic", 'r') as f:
    n, weightMax = map(int,f.readline().split())
    boatPeople = list(map(int,f.readline().split()))
boatPeople.sort()
dq = deque(boatPeople)
count = 0

while dq:
    if len(dq) == 1:
        count +=1
        dq.pop()
        break
    if dq[0] + dq[-1] <= weightMax:
        dq.pop()
        count += 1
    else:
        dq.popleft()
        dq.pop()
        count += 1

print("필요한 최소의 보트는 {}개.".format(count))

