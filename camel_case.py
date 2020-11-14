def camel_case(str):

    return str.replace("_", " ").title().replace(" ", "")

print(camel_case("my_function_name"))