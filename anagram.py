def anagram(str1, str2):

    return sorted(str1.upper().replace(" ", "")) == sorted(str2.upper().replace(" ", ""))


print(anagram("listen","netsil"))


