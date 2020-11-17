def is_goodpw(data):

    if len(data) < 10:
        return False
    if data.isupper() == False:
        return False
    if data.islower() == False:
        return False
    if data.isdigit() == False:
        return False

    return True

# 특수문자 not any 활용

print(is_goodpw("Jjl1sdfasdfqwerqafdsfad"))