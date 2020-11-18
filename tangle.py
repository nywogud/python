from collections import Counter


a = input("N면체 하나는? : ")
b = input("N면체 나머지 다른 하나는? : ")
a = int(a)
b = int(b)

list = []
for i in range(1, a+1):
    for j in range(1, b+1):
        list.append(i+j)

list = Counter(list)
print(list)

for i in range(len(list)):
    max(list.values())
    print(i)

# a = max(list.values())
# result = []
# if list.values() == a:
#     result.append(list.keys())
# print(result)


#Counter({5: 4, 6: 4, 7: 4, 4: 3, 8: 3, 3: 2, 9: 2, 2: 1, 10: 1})



#########################################

# a = input("N면체 하나는? : ")
# b = input("N면체 나머지 다른 하나는? : ")
# a = int(a)
# b = int(b)
# cnt = [0]*(a*b)
# max_val = 0
#
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         index = i+j
#         cnt[index] += 1
#
# #아래의 반복문을 통해 맥스값이 결정됨
# for i in range(a+b+1):
#     if cnt[i] > max_val :
#         max_val = cnt[i]
#
# for i in range(a+b+1):
#     if cnt[i] == max_val :
#         print(i, end=' ')

##############################################

# n, m = map(int, input("n,m을 컴마로 구분해서 입력").split(','))
# if n==m:
#     min_val = n ; max_val = m
# elif n>m:
#     max_val = n; min_val = m
# else :
#     min_val = n ; max_val=m
#
# for i in range(min_val+1, max_val+2):
#     print(i, end=' ')

