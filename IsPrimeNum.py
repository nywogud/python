def isPrimeNum(num):
    num = int(num)
    result = []
    for i in range(1, num+1):
        if num%i==0:
            result.append(i)
        else:
            continue
    result.pop(0)
    result.pop(-1)
    if result:
        return result
    else:
        return "소수임"

num = input("자연수 입력...")
print(isPrimeNum(num))

# 숫자의 제곱근 범위 까지만 뒤져봐도 소수인지 아닌지 알수 있음.
# from math import sqrt
# def isPrime(num):
#     for j in range(2,int(sqrt(num)+1)):
#         if num%j==0:
#             return False
#     return True
# mulPrime = False
#
# N = int(input("숫자입력"))
# for i in range(2, int(sqrt(N)+1)):
#     if isPrime(i):
#         m=N%i
#         if m==0 and isPrime(N//i):
#             print("{} ==> {} *{}".format(N, i, N//i))
#             mulPrime =True
#             break
# if not mulPrime:
#     print("처리불가")


