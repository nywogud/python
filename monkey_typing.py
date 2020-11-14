def monkey_typing(data, word):
    data = sorted(data)

    check_duple = []
    for i in word:
        val = 0
        for j in data:
            if j == i:
                val +=1
        check_duple.append(val)

    return min(check_duple)


print(monkey_typing("apprwtrtwleafdgfafdadfgretdwetpadfadpladfadfaeappleadsfasdfqewrf", "apple"))