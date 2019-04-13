f = open("22.txt", "r")
names = f.read()
names = names.replace('"', '')
names = names.strip('\n').split(',')
names.sort()
ans = 0
for i in range(len(names)):
    tmp = 0
    for j in range(len(names[i])):
        tmp += ord(names[i][j]) - ord('A') + 1
    ans += tmp * (i + 1)
print(ans)