Z, Y, X = map(int, input().split())
count = 0
count = (X-Y)/(Z-Y)
if count == int(count):
    print(int(count))
else:
    print(int(count)+1)

