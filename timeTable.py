timeTable = [(2,3), (6,9),(7,9), (10,12), (4,6), (5,9), (2,11), (3,17)]
timeTable.sort(key=lambda x:(x[1], x[0]))
print(timeTable)