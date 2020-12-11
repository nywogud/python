from collections import deque

with open("./ExData/maxNumber", 'r') as f:
    text = f.readline().split()
    n = int(text[1])
    number = text[0]

print(n)
print(number)
#
# temp = ', '.join(number).split(', ')
# numberLst = []
# for i in temp:
#     numberLst.append(int(i))
# print(numberLst)
#
# Q = numberLst
#
# result = []
#
# cnt = n
# for i in range(0, n):
#     for j in range(0, n):
#         if numberLst[i]<numberLst[j+1]:
#             result.append(numberLst[j+1])
#             cnt -=1
#
#     if cnt == 0:
#         break
#
# print(result)


stack = []

for xx in number:
    while stack and n > 0 and stack[-1] < xx:
        stack.pop()
        n -=1
    stack.append(xx)

if n !=0: # n이 모두 소진되지 않은 경우
    for _ in range(n):
        stack.pop()

result = ''.join(map(str, stack))
print(result)


