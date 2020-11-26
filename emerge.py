# f = open("./ExData/emerg", 'r')
# n, m = map(int, f.readline().split())
# temp = f.readline().split()
# lst = []
# for i in range(len(temp)):
#     lst.append((i, temp[i]))
#
# lst = sorted(lst, key=lambda x : (x[1], x[0]), reverse=True)
#
# lst = [(4, '90'), (3, '80'), (2, '70'), (0, '60'), (1, '50')]
#
#
# print(lst.index(lst[m])+1)

from collections import deque

f = open("./ExData/emerg1", 'r')
n, m = map(int, f.readline().split())

emerLst = [(idx, int(xx)) for idx, xx in enumerate(f.readline().split())]
Q = deque(emerLst)
cnt = 0

while True:
    now = Q.popleft()
    if any(now[1]< x[1] for x in Q):
        Q.append(now)
    else:
        cnt += 1 # 이 사람은 진료 받음.
        if now[0]==m:
            break

print("지정한 {} 환자의 진료 차례는 : {}번째임.".format(m, cnt))
