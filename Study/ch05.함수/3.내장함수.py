"""
날짜 : 2021/1/06
이름 : 양대석
내용 : 파이썬 함수 내장함수 실습하기 교재 p118
"""
import math
import random
import time
#시간 관련 함수
t1 = time.time()
print('t1 : ', t1)  # Unix time

t2 = time.ctime()   # 변환된 Unix time
print('t2 : ', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%yS', now)

print('{}년 {}월 {}일 {}: {}: {}'.format(year, month, date, hour, min, sec))

#수학 관련 함수
r1 = math.ceil(1.2)  #올림
r2 = math.ceil(1.8)

print("r1 : ", r1)
print("r2 : ", r2)

r3 = math.floor(1.2)   # 버림
r4 = math.floor(1.8)

print("r3 : ", r3)
print("r4 : ", r4)

r5 = round(1.2)   #반올림
r6 = round(1.8)

print("r5 : ", r5)
print("r6 : ", r6)

#Random
num1 = random.random()

print('num1 : ', num1)  # 0~1사이의 임의의 실수

num2 = num1 * 10
print('num2 : ', num2)

num3 = math.ceil(num2)
print('num3 : ', num3)

result = math.ceil(random.random()*10)
print('result : ', result)