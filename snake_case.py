def snake_case(str):

    str_invert = ""
    for i in str:
        if i.isupper():
            str_invert += "_{}".format(i)
        elif i.islower():
            str_invert += "{}".format(i)
    str_invert = str_invert.replace("_", "", 1)
    str_invert = str_invert.lower()

    return str_invert

print(snake_case("MyFunctionName"))