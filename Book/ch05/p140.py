# (1) 재귀함수 정의 : 1-n 카운트
def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)
    print(n)

# (2) 함수 호출 1
print('n=0 : ', Counter(0))

# (3) 함수 호출 2
Counter(5)