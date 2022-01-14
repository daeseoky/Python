t = int(input())

for i in range(0, t):
    A, B = map(int, input().split())
    print(A+B)
    if i == t:
        break
