#수행 평가

dataset = [3, 5, 1, 2, 4]
n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            temp = dataset[j]
            dataset[j] = dataset[i]
            dataset[i] = temp




    print(dataset)

print(dataset)