def lastNameAndFirstName(*names): # 여러개의 리스트를 매개변수로 준다.
    for name in names:
        print("{} {}".format(name[0], name[slice(1,10)]))
        print()

lastNameAndFirstName("제갈선희", "곽철용이", "김고오니", "고 광렬이", "저 아세요?")

def vocaList(**words): # 여러개의 딕셔너리를 매개변수로 준다.
    for key, value in words.items():
        print("{0} is {1}".format(key, value))

vocaList(apple = "사과", banana = "바나나")

def furuitStoreBoard(storeName, *messages, **fruitTag):
    '''

    :param storeName: 가게 이름
    :param messages: 오늘 사인보드에 알릴 사항
    :param fruitTag: 과일 가격표
    :return:
    '''

    print("*"*15, storeName, "*"*15, "\n")
    for message in messages:
        print(message)
    print("\n")

    for fruit, tag in fruitTag.items():
        calib = 40-len(fruit)*2 - len(str(tag))
        print("{}".format(fruit), "."*calib, "{}".format(tag))

furuitStoreBoard("jasonBean", "오늘은", "청과들이", "신선합니다.", 사과 =10, 바나나 = 5, \
                 베리 = 20)