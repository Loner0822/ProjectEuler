f = open("13.txt", "r")

sum = 0
while (1):
    num = 0
    line = f.readline()
    if line:
        line = line.strip('\n')
        for i in range(0, len(line)):
            num = num * 10 + int(line[i])
        sum += num
    else:
        break
ans = str(sum)
for i in range(0, 10):
    print(ans[i], end = '')