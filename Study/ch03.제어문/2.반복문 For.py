"""
날짜 : 2021/12/31
이름 : 양대석
내용 : 파이썬 반복문For 실습하기 교재 p70
"""

#for문
# for i in range(5):
#     print('반복 i : ', i)
#
# for j in range(10, 20):
#     print('반복 j : ', j)
#
# for k in range(10, 0, -1):
#     print('반복 k : ', k)
#
#
#
# #1부터 10까지 합
# tot = 0
#
# for i in range(11):
#     tot += i
#
# print('1부터 10까지의 합 : ', tot)
#
# #1부터 10까지 짝수 합
# sum = 0
# for k in range(0, 11, 2):
#     sum += k
#
# print('1부터 10까지 짝수 합 :', sum)
#
# sum, sum1 = 0, 0
# for k in range(0, 11):
#     if k % 2 == 0:
#         sum += k
#     else:
#         sum1 += k
# print('1부터 10까지 짝수 합 :', sum)
# print('1부터 10까지 홀수 합 :', sum1)
#
#
#
# #중첩 for문
# for a in range(3):
#     print('a :', a)
#     for b in range(4):
#         print('b : ', b)
#         for c in range(5):
#             print('c :  ', c)
#
# #구구단
# for a in range(2,10):
#     for b in range(2, 10):
#         c = a * b
#         print('{}단 : {}'.format(a,c))
#
# #별삼각형
# for i in range(1,11):
#
#     for end in range(i):
#         print('☆', end='')
#
#     print()  #줄바꿈
#
# for i in range(11, 0, -1):
#
#     for end in range(i):
#         print('☆', end='')
#
#     print()  #줄바꿈
#
# for i in range(1,11):
#
#     for end in range(11-i):
#         print('☆', end='')
#
#     print()  #줄바꿈

for i in range(11):
    print('★' * i)