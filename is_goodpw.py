import re

def is_goodpw(data):

    if len(data) < 10:
        return False

    if data.islower():
        return False
    if data.islower():
        return False
    i = re.findall('\d', data)
    if bool(i) == False:
        return False

    b = ["!", "@", "#", "$", "%", "^", "&", "*"]

    for i in b:
        for j in data:
            if i == j:
                return True
            else:
                continue
    return False

print(is_goodpw("Ddjkfjeiour1#"))