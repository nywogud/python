# 회의실 예약 시간이 다음 처럼 들어왔을 경우, 최대 몇 팀을 유치할 수 있는지.
# 아래의 예에서는 3을 출력

with open("./ExData/timeTable", 'r') as f:
    a = f.readlines()
    n = len(a)

with open("./ExData/timeTable", 'r') as f:

    meeting = []

    for i in range(n):
        st, et = map(int, f.readline().split())
        meeting.append((st, et))

    meeting.sort(key=lambda x: (x[1], x[0]))
    print(meeting)

    cnt = 0
    et = 0
    for i, j in meeting:
        if i >= et:
            et =j
            cnt += 1
    print("최대 회의 횟수는 : {}".format(cnt))






    # meeting = []
    # for i in range(n):
    #     st, et = map(int, f.readline().split())
    #     meeting.append((st, et))
    #
    # print(meeting)
    #
    # meeting.sort(key=lambda x:(x[1], x[0]))
    # print(meeting)
    #
    # cnt = 0
    # et = 0
    # for s, e in meeting:
    #     if s >= et:
    #         et = e # 이전 미팅의 마지막 시간을 보관
    #         cnt +=1
    #
    # print("회의가 가능한 최대 횟수는 :", cnt)