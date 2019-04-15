coin = [1, 2, 5, 10, 20, 50, 100 ,200]
F = [0] * 201
F[0] = 1

for i in coin:
    for j in range(1, 201):
        if j >= i:
            F[j] += F[j - i]
print(F[200])
