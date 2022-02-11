A = list(input().upper())
B = []
sec = 0
for i in range(len(A)):
    B.append(ord(A[i]))
    for j in B:
        if 65 <= j <=67:
            B[i] = 3
        elif 68 <= j <= 70:
            B[i] = 4
        elif 71 <= j <= 73:
            B[i] = 5
        elif 74 <= j <= 76:
            B[i] = 6
        elif 77 <= j <= 79:
            B[i] = 7
        elif 80 <= j <= 83:
            B[i] = 8
        elif 84 <= j <= 86:
            B[i] = 9
        elif 87 <= j <= 90:
            B[i] = 10

print(sum(B))


#인터넷 풀이법

# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)


