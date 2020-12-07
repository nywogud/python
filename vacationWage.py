def DFS(td, total):
    global maxResult
    if td==n+1:
        if total > maxResult:
            maxResult = total
            print("total = {}".format(total))
    else:
        if td+t[td] <= n+1:
            print("DFS({},{})".format(td + t[td], total + p[td]), end='')
            DFS(td+t[td], total+p[td])

        DFS(td+1, total)

with open("./ExData/vacationWage", 'r') as f:
    n = int(f.readline())
    lst = [list(map(int, f.readline().split())) for _ in range(n)]

print(n)
for i in lst:
    print(i)

t = []
p = []
for i in range(len(lst)):
    t.append(lst[i][0])
    p.append(lst[i][1])
t.insert(0,0)
p.insert(0,0)

print(t)
print(p)

maxResult = 0
DFS(1,0)
print()
print("maxResult : {}".format(maxResult))