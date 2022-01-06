"""
날짜 : 2021/1/04
이름 : 양대석
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p92
"""

# 튜플
dataset = (1, 2, 3, 4, 5)
print('dataset type :', type(dataset))
print('dataset :', dataset)
print('dataset[0] :', dataset[0])
print('dataset[2] :', dataset[2])
print('dataset[3] :', dataset[3])

# 튜플 수정, 추가, 삭제 안됨
dataset[1] = 7   #에러
print('dataset :', dataset)

dataset[2] = []   #에러
print('dataset :', dataset)