# 지금 내 수준에서 낼수 있는 답이나 시간 초과함....
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     cnt = 0
#
#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             continue
#         elif i == 2:
#             cnt += 1
#             continue
#         else:
#             for j in range(2, int(i**0.5)+1):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt += 1
#     print(cnt)
# =======================================================================
# 제한범위내의 모든숫자중에서 소수를 먼저 구하고 지정한 범위의 숫자와 겹칠 경우 카운트 하는 방식
# 이런 방법 생각할 수 있을지 모르겠다
def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

all_list = list(range(2, 246912))
memo = []

for i in all_list:
    if sosu(i):
        memo.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in memo:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())

# ========================================================================

# 내가 푼 방식과유사하나 함수를 이용한 풀이 방식
# def sosu(x):
#     if x == 1:  # 1은 모든 수의 약수이기 때문에 pass
#         return False
#     for i in range(2, int(x ** 0.5) + 1):  # 제곱근이 있는 수 중에
#         if x % i == 0:  # 약수가 있으면 false
#             return False
#     return True  # 이외에는 소수
#
#
# while True:
#     n = int(input())  # 범위를 주기 위한 입력
#     count = 0
#     if n == 0:  # 0 입력하면 아웃되는 게 조건
#         break
#     for i in range(n, 2 * n + 1):  # n과 2n+1사이에서
#         if sosu(i):  # sosu함수안에 있는 게 있다면
#             count += 1  # 카운트를 세라
#     print(count)
