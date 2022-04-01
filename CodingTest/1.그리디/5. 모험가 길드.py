"""
날짜 : 2022/04/01
이름 : 양대석
내용 : 코딩테스트 구현 - 모험가 길드
"""


# N = int(input())
M = sorted(list(map(int, input().split())))

result = 0
count = 0

for i in M:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
print(M)


