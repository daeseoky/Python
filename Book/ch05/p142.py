# (1) 재귀함수 정의 : 1~n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n == 1:  # 종료 조건
        return 1
    else:
        result = n + Adder(n-1)

        print(n, end=' ')
        return result
# (2) 함수 호출 1
print('n=1 : ', Adder(1))

# (2) 함수 호출 2
print('\nn=5 : ', Adder(5))

