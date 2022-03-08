# (1) 래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요')
        func()
        print('잘가요')
    return decorated

# (2) 함수 장식자 적용
@wrap
def hello():
    print('hi ~ ', '홍길동')

# (3) 함수 호출
hello()


