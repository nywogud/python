import operator

newArticle = """
    Local and international experts shared their ideas on how South Korea should set its future diplomatic strategies and North Korea policy following the election of Joe Biden as the 46th U.S. president, during the Kor-Asia Forum 2020, Wednesday.

The forum, co-hosted by The Korea Times and its sister paper the Hankook Ilbo, was held under the theme, "In the Era of Biden: The Future of Asia and the Korean Peninsula," at The Shilla Seoul hotel. While experts here attended the forum in person, those from the U.S., Japan and China participated online due to the COVID-19 pandemic situation.
"""
# "\n"", ",", ".", "\'s" 등등 제거하고 모든 문자 소문자로 바꾸기
newArticle = newArticle.replace("\"", "").replace(",", "").replace(".", "").replace("\'s", "").replace(":", "").lower().split()
print(newArticle)
print()
result = {} # 딕셔너리
for i in range(len(newArticle)):
    cnt = 0
    for j in range(len(newArticle)):
        if newArticle[i]==newArticle[j]:
            cnt += 1
        else:
            result[newArticle[i]]= 1
    result[newArticle[i]] = cnt

result = sorted(result.items(), reverse=True, key=operator.itemgetter(1))
for i in range(len(result)):
    print("{} : {}".format(result[i][0], result[i][1]))

print()

cnt = 1
for i in range(len(result)):
    if cnt == 10:
        break
    print("{} = {}".format(result[i][0], result[i][1]))
    cnt +=1