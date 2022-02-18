Z, Y = map(int, input().split())
X = int(input())

A = Z + (Y + X) // 60
B = (Y + X) % 60

hour = A % 24
print(hour, B)
