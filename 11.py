
f = open("11.txt", "r")

mat = []
for i in range(0, 20):
    line = f.readline()
    vector = line.strip('\n').split(' ')
    mat.append(vector)
f.close()

Max = 0
# up down
for i in range(0, 16):
    for j in range(0, 20):
        tmp = 1
        for k in range(0, 4):
            tmp *= int(mat[i + k][j])
        if Max < tmp:
            Max = tmp
# left right
for i in range(0, 20):
    for j in range(0, 16):
        tmp = 1
        for k in range(0, 4):
            tmp *= int(mat[i][j + k])
        if Max < tmp:
            Max = tmp
# diagonally
for i in range(0, 16):
    for j in range(0, 16):
        tmp = 1
        for k in range(0, 4):
            tmp *= int(mat[i + k][j + k])
        if Max < tmp:
            Max = tmp

for i in range(4, 20):
    for j in range(0, 16):
        tmp = 1
        for k in range(0, 4):
            tmp *= int(mat[i - k][j + k])
        if Max < tmp:
            Max = tmp
print(Max)