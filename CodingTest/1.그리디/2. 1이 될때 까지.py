"""
날짜 : 2022/02/04
이름 : 양대석
내용 코딩테스트 그리드 알고리즘 실습
"""
n, k = map(int, input().split())

result = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1

print(result)