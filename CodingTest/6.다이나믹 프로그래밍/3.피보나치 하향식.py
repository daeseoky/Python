"""
날짜 : 2022/03/25
이름 : 양 대 석
내용 : 다이나믹 프로그래밍 피보나치 상향식(반복문 이용)
"""
import time

# DP((Dynamic Programming) 테이블(메모리제이션을 위한 리스트)
d = [0] * 1000

# 프로그램 실행시간!
start_time = time.time()

# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n

    if d[n] != 0:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)

    return d[n]

for i in range(1000):
    print(fibo(i), end=' ')


# 프로그램 종료 시간!
end_time = time.time()

total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)