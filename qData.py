# x, y  = map(int, input("정수 입력...").split(','))
#
# x, y = 7, 3
# list = []
# for i in range(x):
#     list.append(i+1)
#
# for i in range(len(list)):
#     list.append(list.pop(0))
#     if i ==
# print(list)

#########################################################

# n, k  = map(int, input("정수 입력...").split(','))
# princes = list(range(1, n+1))
#
# while princes:
#     for _ in range(k-1):
#         princes.append(princes.pop(0))
#     print(princes)
#     princes.pop(0)
#
#     if len(princes) == 1:
#         print(princes[0])
#         break

##########################################################
#리스트에서 요소 하나씩 제거하기
#
# lst =[1,2,3,4,5,6,7,8]
# for i in range(len(lst), 0 ,-1):
#     print(lst)
#     lst.remove(i)
#
# print(lst)

#########################################################
# from collections import deque
#
# n, k = map(int, input("정수 입력...").split(','))
# princes = list(range(1, n+1))
# dq = deque(princes)
# while dq:
#     for _ in range(k-1):
#         dq.append(dq.popleft())
#     dq.popleft()
#     if len(dq) == 1:
#         print(dq[0])
#         break
