# A = int(input())%42
# B = int(input())%42
# C = int(input())%42
# D = int(input())%42
# E = int(input())%42
# F = int(input())%42
# G = int(input())%42
# H = int(input())%42
# I = int(input())%42
# J = int(input())%42
#
# L = [A, B, C, D, E, F, G, H, I, J]
# L = set(L)
#
# print(len(L))           #무식한 방법

L = []
for i in range(10):
    n = int(input())
    L.append(n%42)
L = set(L)
print(len(L))
