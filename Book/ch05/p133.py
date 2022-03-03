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


# (1) 함수 클로져


