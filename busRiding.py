f = open("./ExData/busRiding", 'r')
limit, n = map(int, f.readline().split())
lst = []
for i in range(n):
    lst.append(int(f.readline()))

print(limit)
print(n)
print(lst)
finalW = 0

def DFS(index, sum):
    global finalW
    if sum > limit:
        return
    if index == n:
        if sum < finalW:
            finalW = sum
    else:
        DFS(index+1, sum+lst[index])
        DFS(index+1, sum)



DFS(0,0)
print(finalW)