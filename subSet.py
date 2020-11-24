이해가 잘...
def markBit(x,c):
    a=[0]*c
    for i in range(c):
        a[c-i-1]=x%2
        x=x//2
    return a

n = int(input("(부분집합)자연수 입력..."))

tt= [i for i in range(1, n+1)]

for i in range(2**n):
    idx = markBit(2**n-i, n)
    for j in range(n):
        if idx[j] ==1:
            print(tt[j], end='')
    print()