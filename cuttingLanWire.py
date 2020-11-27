# readline 값 하나 있는 경우 하나만 '값'으로 떨어짐. 값 여러개면 '값, 값'
# 중위값을 계속 변경해가며 나올 수 있는 랜선의 갯수를 카운트해서 리스트에 담고 가장 많은 수를 출력

f= open("ExData/CuttingLanWire", 'r')
n, k = map(int, f.readline().split())
lst = []
result = []


for _ in range(n):
    lst.append(int(f.readline()))

f.close()
print(lst)

def LanCable(length):
    cnt = 0
    for x in lst:
        cnt +=(x//length)
        return cnt

lst.sort()
leftMin = 0
rightMax = lst[-1]

while leftMin <= rightMax:
    mid = (leftMin + rightMax)//2
    if LanCable(mid) >=n:
        result.append(mid)
        leftMin = mid+1
    else:
        rightMax = mid -1

print(result)