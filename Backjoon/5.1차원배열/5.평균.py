# t = int(input())
# l = list(map(int, input().split()))
# sum = 0
# max = l[0]
# for i in l[1:]:
#     if i > max:
#         max = i
#
# for i in l[0:]:
#     b = (i / max * 100) / t
#     sum += b
#
# print(sum)

t = int(input())
l = list(map(int, input().split()))
sum = 0
max1 = max(l)

for i in range(t):
    l[i] = (l[i]/max1)*100
    sum += l[i]
print(sum/t)