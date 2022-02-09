n, m = map(int, input().split())

result =0
mins = []
for i in range(n):
    L = list(map(int, input().split()))

    L.sort()
    min = L[0]
    mins.append(min)

mins.sort(reverse=True)
result = mins[0]

print(result)

