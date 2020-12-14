str = "(((()(()()))(())()))(()())"

# def cuttingSteel(str):
#     steel = 0
#     raiser = 0
#     for i in str:
#         if i == "(":
#             steel +=1
#
#         elif i == ")":
#             raiser +=1
#             result = steel*raiser
#     print(result)
#
#
# cuttingSteel(str)


ori = []
for i in str:
    ori.append(i)

print(ori)

stack = []
cnt = 0
for i in range(len(ori)):
    if ori[i] == '(':
        stack.append(ori[i])
    else:
        if ori[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt +=1
print(cnt)

