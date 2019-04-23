Fact = [1]
tmp = 1
for i in range(1, 10):
    tmp *= i
    Fact.append(tmp)

def Check(num):
    res = 0
    tmp = num
    while tmp > 0:
        res += Fact[tmp % 10]
        tmp = int(tmp / 10)
    if res == num:
        return True
    else:
        return False

ans = 0
for i in range(3, 2500000):
    if Check(i):
        ans += i
print(ans)