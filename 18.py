f = open("18.txt", "r")
F = [[0] * 16 for row in range(16)]

for i in range(15):
    line = f.readline()
    line = line.strip('\n').split(' ')
    for j in range(len(line)):
        F[i][j] = int(line[j])

ans = 0
for i in range(15):
    for j in range(i + 1):
        tmp = F[i][j]
        if j < i:
            tmp = max(tmp, F[i][j] + F[i - 1][j])
        if j > 0:
            tmp = max(tmp, F[i][j] + F[i - 1][j - 1])
        F[i][j] = tmp
        ans = max(tmp, ans)
print(ans)

