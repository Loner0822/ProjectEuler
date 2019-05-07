
def Calc(num, step):
    digit = []
    for i in range(step, 0, -1):
        tmp = num * i
        while tmp > 0:
            digit.append(tmp % 10)
            tmp = int(tmp / 10)
            if len(digit) > 9:
                return -1
    if len(digit) != 9:
        return -1
    for i in range(1, 10):
        if i not in digit:
            return -1
    res = 0
    for i in reversed(digit):
        res = res * 10 + i
    return res
    

ans = 0
for i in range(1, 10000):
    for j in range(2, 6):
        ans = max(Calc(i ,j), ans)
print(ans)