def digitSum():

    with open("./ExData/numDigit") as f:
        x = list(map(str, f.readline().split()))
    print(x) # ['4567', '9708', '34', '532']

    result= []
    for i in range(len(x)):
        a = 0
        for j in x[i]:
            a += int(j)
        result.append(a)

    print(result)

    return max(result)

print(digitSum())