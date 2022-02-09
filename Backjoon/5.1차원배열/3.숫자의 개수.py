A = int(input())
B = int(input())
C = int(input())

D = A * B * C
E = list(str(D))
for i in range(10):
    print(E.count(str(i)))



