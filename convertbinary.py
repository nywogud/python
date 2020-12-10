n = int(input("10진수 입력..."))
print(n)

result = []

def DFS(n):
    if n==0:
        return
    else:
        x = n//2
        result.insert(0, n%2)
        DFS(x)

DFS(n)
final =  ""
for i in result:
    final += str(i)

print(final)

#######################################################################

# def DFS(x):
#     if x ==0:
#         return
#     else:
#         DFS(x//2)
#         print(x%2, end='')
#
# n = int(input("10진수 입력..."))
#
# DFS(n)