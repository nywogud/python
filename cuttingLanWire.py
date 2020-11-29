# readline 값 하나 있는 경우 하나만 '값'으로 떨어짐. 값 여러개면 ['5', '10'] 이렇게 나옴
# 중위값을 계속 변경해가며 나올 수 있는 랜선의 갯수를 카운트해서 리스트에 담고 가장 많은 수를 출력

# f= open("ExData/CuttingLanWire", 'r')
# n, k = map(int, f.readline().split())
# lst = []
# result = []
#
#
# for _ in range(n):
#     lst.append(int(f.readline()))
#
# f.close()
#
# def LanCable(length):
#     cnt = 0
#     for x in lst:
#         cnt +=(x//length)
#     return cnt
#
# lst.sort()
# print(lst)
# leftMin = 0
# rightMax = len(lst)-1
#
# while leftMin <= rightMax:
#     mid = (leftMin + rightMax)//2
#     if LanCable(mid) >=n:
#         result.append(mid)
#         leftMin = mid+1
#     else:
#         rightMax = mid -1
#
# print(result)
#
# 알고리즘은 아래와 같습니다.
#
# 1. 입력 받은 전선의 길이 중 최대 길이를 high로 잡습니다.
#
# 2. 자르는 전선의 길이가 존재해야하므로 low는 1로 잡습니다.
#
# 3. 이분 탐색을 진행하면서 mid에 대해 조건을 충족하는지 확인합니다.
#
# i) 조건이 충족된다면 자르는 전선의 길이를 늘립니다.
#
# ii) 조건이 충족되지 않는다면 자른는 전선의 길이를 줄입니다.
#
# 4. 조건이 충족되는 최대 길이를 출력합니다.

#############################################################

# f = open("./ExData/CuttingLanWire", 'r')
# n, k = map(int,f.readline().split())
# lst = list(int(f.readline()) for _ in range(n))
# print("{}, {}".format(n, k))
# lst.sort()
# print(lst)
#
# # def median(lst):
# if len(lst)%2 == 0: #짝수
#     a = len(lst)//2
#     median = (lst[a]+lst[a-1])/2
# else:
#     b = len(lst)//2
#     median = lst[b]
#
# print(median)
#
# key = int(input("찾고자 하는 숫자 입력"))
# left = 0;
# right = len(lst)-1
#
# while left <= right:
#     mid = (left + right)//2
#     if key == lst[mid]:
#         print("찾고자 하는 숫자 {}은 인덱스 {}번 임.".format(key, mid))
#         break
#     elif key < lst[mid]:
#         right = mid - 1
#     elif key > lst[mid]:
#         left = mid + 1
#
# print("찾는 값이 없음.")

f = open("./ExData/CuttingLanWire", 'r')
k, n = map(int,f.readline().split())
lst = list(int(f.readline()) for _ in range(k))
print("{}, {}".format(n, k))
lst.sort()
print(lst)
start, end = 1, max(lst)  # 이분탐색 처음과 끝위치

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    print("start : {}".format(start))
    print("end : {}".format(end))
    mid = (start + end) // 2  # 중간 위치
    print(mid)
    lines = 0  # 랜선 수
    for i in lst:
        lines += i // mid  # 분할 된 랜선 수
    print(lines)
    if lines >= n:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)




