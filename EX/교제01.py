import random


def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0, 1)
        if r == 1:
            result.append(1)
        else:
            result.append(0)

    return result


print(coin(10))
