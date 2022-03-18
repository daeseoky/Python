# 방법은 맞는거 같은데.... 시간초과 그래서 찾아보고 2~i까지 검사하는게 아니라 2~i제곱근까지만 검사
Z, Y = map(int, input().split())

for i in range(Z, Y+1):
    if i != 1:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            print(i)

