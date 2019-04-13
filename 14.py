def ChainLen(num):
    res = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        res += 1
    return res + 1
Max = 0
ans = 0
for i in range(1, 1000001):
    tmp = ChainLen(i)
    if tmp > Max:
        Max = tmp
        ans = i
print(ans)