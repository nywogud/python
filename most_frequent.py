def most_frequent(list):
    maximum = []
    for i in range(len(list)):
        maximum.append(list.count(list[i]))

    return list[maximum.index(max(maximum))]

print(most_frequent(["e", "c", "b","b", "aaa", "aaa"]))