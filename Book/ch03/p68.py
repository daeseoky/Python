import random

help(random.randint)
help(random.choices)

name = ['이순신', '홍길동', '유관순']

print(name)
print(name[2])

if '유관순' in name:
    print('유관순 있음')
else:
    print('유관순 없음')

idx = random.randint(0,2)
print(name[idx])