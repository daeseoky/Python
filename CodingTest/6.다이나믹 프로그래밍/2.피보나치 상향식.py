"""
날짜 : 2022/03/25
이름 : 양 대 석
내용 : 다이나믹 프로그래밍 피보나치 상향식(반복문 이용)
"""
import time

# 프로그램 실행시간!
start_time = time.time()

# DP((Dynamic Programming) 테이블
d = [0] * 10000
d[0] = 0
d[1] = 1


# 피보나치 반복문
for i in range(2, 10000):
    d[i] = d[i-1] + d[i-2]
    print(d[i], end=' ')


print()

# 프로그램 종료 시간!
end_time = time.time()

total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)