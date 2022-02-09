# A = int(input())
#
# for i in range(A):
#     B = map(int, input().split())
#     l = list(B)
#     sum = 0
#     cnt = 0
#     for j in l[1:]:
#         sum += j
#     mean = sum / l[0]
#
#     for k in l[1:]:
#         if mean < k:
#             cnt += 1
#     f = cnt / l[0] * 100
#
#     print('%.3f' %f+'%')


for i in range(int(input())):
    B = list(map(int, input().split()))
    sum = 0
    cnt = 0

    for j in B[1:]:
        sum += j
    mean = sum / B[0]

    for k in B[1:]:
        if mean < k:
            cnt += 1
    f = cnt / B[0] * 100

    print('%.3f' % f + '%')
