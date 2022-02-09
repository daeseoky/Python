z = set(range(10000))
y = set()

for i in z:
    a = i % 10
    b = (i // 10) % 10
    c = (i // 100) % 10
    d = i // 1000
    e = i + a + b + c + d
    y.add(e)

x = sorted(z - y)

for i in x:
    print(i)

