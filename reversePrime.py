Q = [32, 55, 62, 3700, 350]

def reverse(lst):
    temp = ''
    for i in lst:
        temp += str(i)
        temp += ', '
    a = ''.join(reversed(temp))
    print(a)
    b = a.replace(" ,", "", 1)
    print(b)
    c = b.split(',')
    print(c)
    tempLst = []
    for i in c:
        tempLst.append(int(i))
    isPrimeNum(tempLst)

#소수 구하기 함수
def isPrimeNum(x):
    for i in x:
        temp =[]
        for j in range(1, i+1):
            if i%j==0:
                temp.append(j)

        temp.pop(0)
        temp.pop(-1)
        print(temp)


reverse(Q)