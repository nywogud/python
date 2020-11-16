def is_goodpw(data):

    if len(data) < 10:
        return False
    elif data.isupper():
        return False
    elif data.islower():
        return False
    elif data.isdigit():
        return False
    else:
        return True

# 특수문자 not any 활용

print(is_goodpw("Jjl1sdfasdfqwerqafdsfad"))