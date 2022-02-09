t = int(input())
l = list(map(int, input().split()))
min = l[0]
max = l[0]
for i in l[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)
