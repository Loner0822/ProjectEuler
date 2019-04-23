import math

def equals(num1, num2):
    if math.fabs(num1 - num2) < 1e-6:
        return True
    else:
        return False

def gcd(x, y):
    if y != 0:
        return gcd(y, x % y)
    else:
        return x

fz = 1
fm = 1
for i in range(1, 10):
    for j in range(i + 1, 10):
        for k in range(1, 10):
            if equals((i * 10 + k) / (j * 10 + k), i / j):
                fz *= (i * 10 + k)
                fm *= (j * 10 + k)
                continue
            if equals((i * 10 + k) / (k * 10 + j), i / j):
                fz *= (i * 10 + k)
                fm *= (k * 10 + j)
                continue
            if equals((k * 10 + i) / (j * 10 + k), i / j):
                fz *= (k * 10 + i)
                fm *= (j * 10 + k)
                continue
            if equals((k * 10 + i) / (k * 10 + j), i / j):
                fz *= (k * 10 + i)
                fm *= (k * 10 + j)
                continue
print(int(fm / gcd(fm, fz)))