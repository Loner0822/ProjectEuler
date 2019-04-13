n = 1001
n = int(n / 2)
tmp = 1
ans = 1
for i in range(n):
    for j in range(4):
        tmp += (i + 1) * 2
        ans += tmp
print(ans) 