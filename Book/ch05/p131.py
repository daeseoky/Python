# lambda 매개변수 : 실행문(반환값)

# (1) 일반 함수
def Adder(x, y):
    add = x + y
    return add


print('add :', Adder(10, 20))

# (2) 람다 함수
a = (lambda x, y : x + y)(10, 20)
print('add :', a)

print('add :',(lambda x, y : x + y)(10, 20))
