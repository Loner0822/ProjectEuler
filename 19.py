Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Day = 1
ans = 0
for Year in range(1900, 2001):
    if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
        Month[1] = 29
    else:
        Month[1] = 28
    for i in range(len(Month)):
        Day += Month[i]
        Day %= 7
        if Day == 0:
            if Year + int((i + 1) / 12) >= 1901 and Year + int((i + 1) / 12) < 2001:
                ans += 1
print(ans)