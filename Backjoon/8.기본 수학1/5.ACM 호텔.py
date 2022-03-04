A = int(input())

for i in range(A):
    X, Y, Z = map(int, input().split())

    if Z % X == 0:
        B = Z // X
        C = X * 100
    else:
        B = (Z // X) + 1
        C = (Z % X) * 100
    print(B + C)

