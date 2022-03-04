"""
중첩 함수
def 외부함수(인수)
    실행문
    def 내부함수(인수)
        실행문
        return 값
    return 내부함수
"""
# (1) 일급 함수
def a():  # outer
    print('a 함수')
    def b():  # inner
        print('b 함수')
    return b
b = a()  # 외부 함수 호출 : a 함수
b()      # 내부 함수 호출 : b 함수


# (2) 함수 클로져
data = list(range(1, 101))
def outer_func(data):
    dataSet = data  # 값(1~100) 생성

    # inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val

    return tot, avg   # inner 반환

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부 함수 호출
tot_val = tot()
print('tot :', tot_val)
avg_val = avg(tot_val)
print('avg :', avg_val)


