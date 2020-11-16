def select_common(str1, str2):

    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = str1.split(",")
    str2 = str2.split(",")
    str_arr = []
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
               str_arr.append(str1[i])
            else:
                continue
    return ','.join(str_arr)



def select_common1(str1, str2):
    aset, bset = set(str1.replace(" ","").split(",")), set(str2.replace(" ","").split(","))
    return ','.join(sorted(aset & bset))


print(select_common("one, two, three", "two, five, six, one"))