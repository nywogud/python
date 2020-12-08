f= open("./ExData/maxK", 'r')
n, k = map(int, f.readline().split())
lst = list(map(int, f.readline().split()))

print(n)
print(k)
print(lst)

lst.sort(reverse=True)

print(lst)

result =[]
for i in range(0,n):
    for j in range(1,n):
        for x in range(2,n):
            result.append(lst[i] + lst[j] + lst[x])
            print("lst[i] : {}, lst[j] : {}, lst[x] : {}".format(lst[i], lst[j], lst[x]))

print(result)
result.sort(reverse=True)
print(result)
result = set(result)
print(result)
result = sorted(list(result), reverse=True)
print(result)

#####################################################

# f = open("./ExData/maxK", 'r')
# n, k = map(int, f.readline().split())
# arr = list(map(int, f.readline().split()))
#
# print(arr)
# sumList = set()
# for i in range(n):
#     for j in range(i+1, n):
#         for l in range(j+1,n):
#             sumList.add(arr[i] + arr[j] + arr[j]) # 추가되면서 중복이 제거됨.
#
# print(sumList)
# sumList = list(sumList)
# sumList.sort(reverse=True)
# print(sumList)
# print("세번째 큰 수는 : {}".format(sumList[k-1]))
