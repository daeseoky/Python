Z, Y, X = map(int, input().split())

if Z == Y == X:
    print(10000+Z*1000)
elif Z == Y != X:
    print(1000+Z*100)
elif Z != Y == X:
    print(1000+Y*100)
elif Z == X != Y:
    print(1000+X*100)
else:
    print(max(Z, Y, X)*100)

# set 쓸생각을 못했음 그나마 이게 깔끔해보임
temp=input().split(" ") # 값을 받아옴(문자열)
list=[]
for i in temp:
    list.append(int(i)) # 정수형으로 바꿔서 list라는 배열에 넣음
list.sort() # 리스트 정렬
list_s = set(list) # 리스트를 집합화 시켜주고 list_s에 넣어줌

if len(list_s)==1 : # 모두 같은눈이 나왔을 때
    print(10000+list[0]*100)
elif len(list_s)==3 : # 모두 다른눈이 나왔을 때
    print(list[-1]*100)
else : # 2개가 같은눈이 나왔을 때
    print(1000+list[1]*100)  # 총 3개의 원소 중 정렬을 했을 때 중간이 같은수