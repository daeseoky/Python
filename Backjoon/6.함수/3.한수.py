def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        a = (i // 100) % 10
        b = (i // 10) % 10
        c = i % 10
        if i < 100:
            cnt += 1
        elif 99 < i < 1000:
            if a - b == b - c:
                cnt += 1
    return cnt


num = int(input())
print(hansu(num))

