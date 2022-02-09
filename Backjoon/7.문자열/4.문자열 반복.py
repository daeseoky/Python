Z = int(input())

for i in range(Z):
    A, B = (input().split())
    a = int(A)
    for j in B:
        print(j * a, end='')
    print()


