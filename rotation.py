# n = int(input("자연수 n 입력...."))
n = 15

def DFS(step):
    if step > n:
        return
    else:
        # print(step, end=' ') 전위순회
        DFS(step*2)
        # print(step, end=' ') 중위순회
        DFS(step*2+1)
        # print(step, end=' ') 후위순회

DFS(1)