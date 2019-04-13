import math

def Check_Prime(num):
    if num < 2 or num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True

Max = 0
ans = 0
for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        len = 0
        for k in range(0, 80):
            if Check_Prime(k * k + i * k + j):
                continue
            else:
                len = k - 1
                break
        if len > Max:
            Max = len
            ans = i * j
print(ans)