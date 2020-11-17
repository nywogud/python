# 로토번호 추출기 1~45 중 6개 추출 중복 안됨
import random
def lotto():
    ran = []
    i = 0
    while(i<6):
        x = random.randrange(1,45)
        if x not in ran:
            ran.append(x)
            i = i + 1
        else:
            continue

    return ran

def lotto1():
    lotto = []
    while len(set(lotto)) != 6:
        xx = random.randint(1,45)
        lotto.append(xx)
    return set(lotto)

def lotto2():
    return random.sample(range(1,46),6)

print(lotto2())

