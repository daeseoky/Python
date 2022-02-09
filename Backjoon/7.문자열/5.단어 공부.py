A = input().upper()
B = list(set(A))
D = []

for i in B:
    C = A.count(i)
    D.append(C)

if D.count(max(D)) > 1:
    print('?')
else:
    E = D.index(max(D))
    print(B[E])


