l = []

for i in range(9):
    l.append(int(input()))

ma = l[0]
for i in l[1:]:
    if i > ma:
        ma = i

print(ma)
print(l.index(ma)+1)



