with open("./ExData/storage", 'r') as f:
    x = int(f.readline())
    lst = list(map(int, f.readline().split()))
    n = int(f.readline())

    lst = sorted(lst)

    for i in range(n):
        lst[0] += 1
        lst[-1] -= 1
        lst = sorted(lst)
        print(lst)

print(lst[-1]-lst[0])

with open("./ExData/storage1", 'r') as f:
    x = int(f.readline())
    lst = list(map(int, f.readline().split()))
    n = int(f.readline())

    lst = sorted(lst)

    for i in range(n):
        lst[0] += 1
        lst[-1] -= 1
        lst = sorted(lst)
        print(lst)

print(lst[-1]-lst[0])