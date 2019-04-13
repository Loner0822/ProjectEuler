C = [[0] * 21 for row in range(21)]
C[0][0] = 1

for i in range(0, 21):
    for j in range(0, 21):
        if i > 0:
            C[i][j] += C[i - 1][j]
        if j > 0:
            C[i][j] += C[i][j - 1]
print(C[20][20])