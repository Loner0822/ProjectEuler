def Check(num):
    Base_10 = []
    Base_2 = []
    Base_tmp = []
    tmp = num
    while tmp > 0:
        Base_10.append(tmp % 10)
        Base_tmp.insert(0, tmp % 10)
        tmp = int(tmp / 10)
    if Base_10 != Base_tmp:
        return False
    Base_tmp = []
    tmp = num
    while tmp > 0:
        Base_2.append(tmp % 2)
        Base_tmp.insert(0, tmp % 2)
        tmp = int(tmp / 2)
    if Base_2 != Base_tmp:
        return False
    return True

ans = 0
for i in range(1, 1000000):
    if Check(i):
        ans += i
print(ans)