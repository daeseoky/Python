"""
날짜 : 2021/1/06
이름 : 양대석
내용 : 파이썬 파일 입출력 실습하기 교재 p217
"""

# 파일 읽기
f1 = open('./Test.txt', mode='r', encoding='utf-8')

while True:
    # 줄단위 읽기
    line = f1.read()

    if not line:
        break

    print(line)

f1.close()

# 파일 쓰기
f2 = open('./Result.txt', mode='w', encoding='utf-8')
f2.write('안녕하세요.\n')
f2.write('반갑습니다.\n')
f2.write('감사합니다.\n')
f2.close()

#구구단 쓰기

f3 = open('./Gugudan.txt', mode='w', encoding='utf-8')

for i in range(2, 10):
    f3.write('%d단\n' % i)
    for j in range(2, 10):
        z = i * j
        f3.write('{} x {} = {}\n'.format(i, j, z))


