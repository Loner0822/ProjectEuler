
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

dic = {}
for i in range(1, 10000):
    dic[i] = DivisorSum(i)
ans = 0
for i in range(1, 10000):
    if dic.get(dic[i], 0) == i and dic[i] != i:
        ans += i
print(ans)