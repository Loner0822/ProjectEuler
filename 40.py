d = [0]
num = 1

while True:
    tmp = num
    dig = []
    while tmp > 0:
        dig.append(tmp % 10)
        tmp = int(tmp / 10)
    dig.reverse()
    for i in dig:
        d.append(i)
    if len(d) > 1000000:
        break
    num = num + 1
print(d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000])