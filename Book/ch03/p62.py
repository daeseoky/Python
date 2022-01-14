score = int(input('점수 입력:'))
grade = ''
if 85 <= score <= 100:
    grade = '우수'
elif 70 <= score < 85:
    grade = '보통'
else:
    grade = '저조'

print('당신의 점수는 %d 점이고, 등금은 %s' %(score, grade))