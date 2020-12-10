from collections import deque

f = open("./ExData/lecture", 'r')
x = f.readline().split()
print(x)
x = list(''.join(x[0]))
print(x)
n = int(f.readline())
print(n)
temp = []
for _ in range(n):
    temp.append(f.readline().split())

print(temp)

lst= []
for i in range(len(temp)):
    lst.append(list(''.join(temp[i][0])))
print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        print(lst[i][j])

print()
for i in x:
    print(i)


# TypeError: 'collections.deque' object cannot be interpreted as an integer
for z in x:
    result = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == z:
                result.append(z)
                print(result)

        # if result == x:
        #     print("YES")
        # else:
        #     print("NO")


############################################
# from collections import deque
# f = open("./ExData/lecture", 'r')
# major = f.readline()
# print(major)
# n = int(f.readline())
# print(n)
# for i in range(n):
#     schedule = f.readline()
#     dq = deque(major)
#     for xx in schedule:
#         if xx in dq: # 순서를 체크하는 부분
#             if xx != dq.popleft():
#                 print("#{} : NO".format(i+1))
#                 break
#     else:
#         if len(dq) == 0:
#             print("#{} : YES".format(i+1))
#         else :
#             print("#{} : NO".format(i+1)) # 예를들어 C,B,  만족하면
