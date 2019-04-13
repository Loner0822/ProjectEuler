ans = 0
for i in range(2, 999999):
    num = 0
    tmp = i
    while tmp > 0:
        num += int(pow(tmp % 10, 5))
        tmp = int(tmp / 10)
    if num == i:
        ans += num
print(ans)