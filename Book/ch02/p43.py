# 문자형 숫자 입력
num = input('숫자 입력 : ')
print('numtype : ', type(num))
print(num)
print(num*2)

# 문자형 숫자를 정수형으로 입력
num1 = int(input('숫자 입력 : '))
print(num1*2)

# 문자형 숫자를 실수형으로 입력
num2 = float(input('숫자 입력 : '))
result = num1 + num2   # 실수 = 정수 + 실수
print('result = ', result)
