A = list(input())
B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
C = []
#
# for i in B:
#     if i in A:
#         print(A.index(i), end=" ")
#     else:
#         print(-1, end=" ")

# 내가 푼 방법
for i in B:
    if i in A:
        C += [A.index(i)]  #index 찾는 문자 or 숫자가 없으면 에러
    else:
        C += [-1]

for i in C:
    print(i, end=' ')

# # '아스키코드'를 이용한 방법
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위
#
# for x in alphabet :
#     print(word.find(chr(x)), end=' ')   #find는 문자열에서만 사용가능 찾는 문자가 없으면 -1출력
