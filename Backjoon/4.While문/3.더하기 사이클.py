T = int(input())
count = 0
A = T
while 1:
    T = ((T % 10) * 10) + (((T // 10) + (T % 10)) % 10)
    count += 1

    if A == T:
        break

print(count)

