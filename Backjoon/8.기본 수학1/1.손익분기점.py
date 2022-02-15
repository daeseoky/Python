A, B, C = map(int, input().split())

try:
    X = A//(C-B)+1

    if X > 0:
        print(X)
    else:
        print(-1)

except ZeroDivisionError:
    print(-1)


# 인터넷 정답
# A, B, C = map(int, input().split())
#
# if B >= C:
#     print(-1)
# else:
#     print(int(A/(C-B)+1))


