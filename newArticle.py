from collections import Counter

newArticle = """

Justice Minister Choo Mi-ae on Tuesday suspended Prosecutor General Yoon Seok-youl from his duty, in an unprecedented move amid a feud over prosecution reforms and various investigations involving Yoon's aide and family members.

"The ministry has been investigating various allegations against the top prosecutor and found out some serious misconduct," the justice minister said during a briefing.

As reasons to bar him from his duty and seek disciplinary actions, the minister cited what she called an "improper" meeting with a media executive, the illegal inspection of judges involved in controversial cases, interference with the prosecution's investigations to protect people close to him and damage to public trust in the political neutrality of the prosecution. She also cited his alleged leak of information to the press on the Supreme Prosecutors Office's launch of an audit into his close aide involved in an alleged blackmail case.

She said that Yoon violated ethics by meeting with Hong Seok-hyun, chairman of JoongAng Holdings, the media group that owns local daily JoongAng Ilbo and cable channel JTBC, in November 2018, who could be an interested party in a case being probed by prosecutors. Yoon was the chief prosecutor at the Seoul Central District Prosecutors Office at that time. Choo didn't offer further details.

She also said Yoon had impeded the ministry's lawful probe by not responding to recent written investigation inquiries.

"As the justice minister, who has the utmost authority to oversee the prosecution, I decided that it is not tolerable to let him continue his duty," Choo said.

"""
#
# newArticle=newArticle.split()
#
# prequent = Counter(newArticle)
# print(prequent.most_common(10))

#######################################################

# newArticle=newArticle.split(' ')
# print(newArticle)
# frequent = []
#
# for i in range(len(newArticle)):
#     cnt = 0
#     for j in range(len(newArticle)):
#         if newArticle[i] == newArticle[j]:
#             cnt += 1
#             frequent.append((newArticle[i], cnt))
#
# print(frequent)
###################################################################
# "\n"", ",", ".", "\'s" 등등 제거
newArticle.re(",", "")

print(newArticle)

# newArticle=newArticle.split()
#
#
#
# print(newArticle)