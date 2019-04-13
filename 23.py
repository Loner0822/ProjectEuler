def DivisorSum(num):
    res = 0
    tmp = 1
    while True:
        if tmp * tmp > num:
            break
        if num % tmp == 0:
            if int(num / tmp) == tmp:
                res += tmp
            else:
                res += tmp + num / tmp
        tmp += 1
    return int(res - num)

abu_list = []
for i in range(1, 28124):
    if DivisorSum(i) > i:
        abu_list.append(i)

vis = [0] * 28124
for i in abu_list:
    for j in abu_list:
        if i + j <= 28123:
            vis[i + j] = 1

ans = 0
for i in range(1, 28124):
    if vis[i] == 0:
        ans += i
print(ans)