"""
날짜 : 2021/12/31
이름 : 양대석
내용 : 파이썬 반복문 While 실습하기 교재 p64
"""

# #while문
# i = 1
#
# while i <= 5:
#
#     print('반복 i : ', i)
#     i +=1
#
# #1부터 10까지 합
# tot, k = 0, 1
#
# while k <= 10:
#     tot += k
#     k += 1
# print('1부터 10까지 합 : ',tot)
#
# #1부터 10까지 홀수합
# tot, k = 0, 1
# while k<=10:
#     if k % 2 == 1:
#         tot += k
#     k += 1
# print('1부터 10까지 홀수합 :', tot)

#break
num = 1

while True:

    if num % 5==0 and num % 7==0:
        break

    num += 1

print('5와 7의 최소공배수 : ', num)

#continue
n = 0

while n <= 10:

    n += 1
    if n % 2 == 0:
        continue

    print(n, end=', ')






#while문