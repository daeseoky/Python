Z = int(input())

sosu = []

for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosu.append(i)

# print(sosu)  소수 수집은 이상없음

for i in range(Z):
    Y = int(input())
    for j in sosu:
        for k in sosu:
            if j + k == Y:
                print(j, k)
                break

