"""
날짜 : 2021/1/04
이름 : 양대석
내용 : 파이썬 기본 입출력
"""

# 이름, 나이, 생년월일 출력
name = input('이름 입력 : ')
age = input('나이 입력 : ')

year = 2021 - int(age) + 1
year = str(year)

print(name+'님은 '+age+'세이고'+year+'년도에 태어 났습니다.')
