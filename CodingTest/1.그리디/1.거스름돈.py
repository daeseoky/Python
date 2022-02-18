"""
날짜 : 2022/02/04
이름 : 양대석
내용 코딩테스트 그리드 알고리즘 실습
"""

n = 1260
count = 0
array = [500, 100, 50, 10]

for i in array:
    count += n // i
    n %= i

print(count)