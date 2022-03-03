# (1) 인수가 없는 함수
def userfunc1():
     print('인수가 없는 함수')
     print('userFunc1')

userfunc1()

# (2) 인수가 있는 함수
def userfunc2(x, y):
     print('userFunc2')
     z = x + y
     print('z=', z)

userfunc2(10, 20 )

# (3) return 있는 함수
def userfunc3(x, y):
     print(userfunc3)
     tot = x + y
     sub = x - y
     mul = x * y
     div = x / y

     return tot, sub, mul, div

#실인수 키보드 입력
x = int(input())
y = int(input())

t, s, m, d = userfunc3(x, y)


print('t : ', t)
print('s : ', s)
print('m : ', m)
print('d : ', d)