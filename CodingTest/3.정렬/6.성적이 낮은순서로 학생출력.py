Z = int(input())
A = []
for i in range(Z):
    B = list(input().split())
    A.append(B)

result = sorted(A, key=lambda data: data[1])

for i in range(Z):
    print(result[i][0], end=" ")

for j in result:
    print(j[0], end=" ")

