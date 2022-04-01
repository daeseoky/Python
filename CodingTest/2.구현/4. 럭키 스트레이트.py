"""
날짜 : 2022/04/01
이름 : 양대석
내용 : 코딩테스트 구현 - 럭키 스트레이트
"""
#데이터 입력받기
n = list(map(int, input()))
a = int(len(n) / 2)
t1 = 0
t2 = 0

for i in n[:a]:
    t1 += i
for i in n[a:]:
    t2 += i

if t1 == t2:
    print('LUCKY')
else:
    print('READY')









