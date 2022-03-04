Z = int(input())

bag = 0
while Z >= 0:
    if Z % 5 == 0:
        bag += Z / 5
        print(int(bag))
        break
    Z -= 3
    bag += 1
else:
    print(-1)

