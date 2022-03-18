Z, Y = map(int, input().split())
M = list(map(int, input().split()))
M.sort()

start = 0
end = M[Z-1]

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in M:
        if i > mid:
            total += i - mid
    if total < Y:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)








