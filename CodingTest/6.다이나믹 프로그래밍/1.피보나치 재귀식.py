"""
날짜 : 2022/03/25
이름 : 양 대 석
내용 : 다이나믹 프로그래밍 피보나치 재귀식
"""
import time

# 프로그램 실행시간!
start_time = time.time()


# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n

    return fibo(n-1) + fibo(n-2)

print(fibo(39))


#프로그램 종료 시간!
end_time = time.time()

total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)