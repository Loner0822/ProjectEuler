ans = 0
Max = 0
for i in range(2, 1000):
    cnt = 0
    res = 1
    dic = {}
    while dic.get(res, 0) == 0:
        dic[res] = 1
        res *= 10
        res %= i
        cnt += 1
    if res != 0 and Max < cnt:
        Max = cnt
        ans = i
print(ans)
