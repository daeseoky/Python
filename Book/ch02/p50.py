# 왼쪽 기준
oneline = 'this is one line string'

print(oneline)
print('문자열 길이 : ', len(oneline))
print(oneline[0:4])
print(oneline[:4])
print(oneline[:])    #전체
print(oneline[::2])
# 오른쪽 기준
print(oneline[0:-1:2])
print(oneline[-6:-1])
print(oneline[-6:])

# 부분 문자열 생성
substring = oneline[-11:]
print(substring)