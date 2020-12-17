with open("./ExData/changeDigit", 'r') as f:
    lst = [list(map(int, f.readline().split())) for _ in range(10)]

print(lst)
num = 0
card = []
for _ in range(20):
    num += 1
    card.append(num)

print(card)

def changeDigit(lst):
    for i in lst:
        temp = card[(i[0]-1): i[1]]
        print(temp)
        temp.reverse()
        print(temp)
        for x in range(i[1]-i[0]+2):
            for j in temp:
                card[x] = j
        print(card)


changeDigit(lst)