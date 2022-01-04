# 외부 상수 인수
name = '홍길동'
age = 35
price = 123.456
print('이름 {}: , 나이 {}: ,data : {}'.format(name, age, price))

#format 축약형(SQL문 작성)
uid = input('id : input: ')
query = f"select * from member where uid = {uid}"
print(query)   #member 테이블에서 uid가 hong인 레코드 검색