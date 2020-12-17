import numpy as np
x = np.arange(100).reshape(10,10)

print(x)
print()

print(x[5][3:6])
print()

print(x[8][[2, 4, 8]]) # fancy indexing
print()

np.random.seed(52)
x = np.array(np.random.randint(55, size=10))
print(x)
print()

idx = np.argsort(x) # 정렬된 요소들의 인덱스 반환
print(idx)
print()

ar = np.arange(64).reshape(4,16)
print(ar)
print()
print(ar.T)
print()
x = np.dot(ar, ar.T)
print(x)
x = x[0:3, 1:4]
print(x)
print()
print(x[0, 2])