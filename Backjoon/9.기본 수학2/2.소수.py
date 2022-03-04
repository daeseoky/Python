Z = int(input())
Y = int(input())
A = []

for num in range(Z, Y+1):
    if num != 1:
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            A.append(num)
if sum(A) != 0:
    print(sum(A))
    print(A[0])
else:
    print(-1)


