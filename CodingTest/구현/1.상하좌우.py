A = int(input())
Z = [1, 1]

B = list(input().split())
for j in B:
    if j == 'L':
        if Z[1] <= 1:
            continue
        else:
            Z[1] -= 1

    if j == 'R':
        if Z[1] >= A:
            continue
        else:
            Z[1] += 1

    if j == 'U':
        if Z[0] <= 1:
            continue
        else:
            Z[0] -= 1

    if j == 'D':
        if Z[0] >= A:
            continue
        else:
            Z[0] += 1

print(Z)
