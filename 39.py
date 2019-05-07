ans = 0
num = 0
for p in range(3, 1001):
    cnt = 0
    for a in range(1, p):
        for b in range(1, a):
            c = p - a - b
            if c > b:
                continue
            if c * c + b * b == a * a and c > 0:
                cnt += 1
    if cnt > ans:
        ans = cnt
        num = p
print(p, num)