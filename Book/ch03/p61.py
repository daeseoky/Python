var = 10
if var >= 5:
    print('var=', var)
    print('var는 5보다 크다')
    print('조건이 참인 경우 실행')

print('항상 실행')


# 100~85 : 우수, 84~70 : 보통, 69 : 저조
score = int(input('점수 입력 : '))
if 85 <= score <= 100:
    print('우수')
elif 70 <= score < 85:
    print('보통')
else:
    print('저조')