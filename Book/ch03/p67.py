import random
help(random)  # 묘듈 도움말

help(random.random)  #random모듈의 random함수의 도움말

r = random.random()  #random.random은 0과 1사이의 난수

print("r : ", r)


cnt = 0

while True:
    r = random.random()
    print(r)
    if r < 0.01:
        break
    else:
        cnt += 1

print('난수 갯수 : ', cnt)


