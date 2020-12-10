from collections import deque

with open("./ExData/vocaMatching", 'r') as f:
    n = int(f.readline())
    voca = []
    for _ in range(2*n-1):
        voca.append(f.readline().replace("\n", ""))

print(n)
print(voca)

q = deque(voca)
vocaCom = set(voca)
print(vocaCom)

for i in range(len(q)):
    for j in vocaCom:
        if q[i] == j:
            q.pop()


print(q)

#
# for i in voca:
#     if voca.count(i) == 1:
#         print(i)