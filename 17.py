dic = {}
dic[1] = 3
dic[2] = 3
dic[3] = 5
dic[4] = 4
dic[5] = 4
dic[6] = 3
dic[7] = 5
dic[8] = 5
dic[9] = 4
dic[10] = 3
dic[11] = 6
dic[12] = 6
dic[13] = 8
dic[14] = 8
dic[15] = 7
dic[16] = 7
dic[17] = 9
dic[18] = 8
dic[19] = 8
dic[20] = 6
dic[30] = 6
dic[40] = 5
dic[50] = 5
dic[60] = 5
dic[70] = 7
dic[80] = 6
dic[90] = 6
dic[100] = 7
dic[1000] = 8

ans = 0
for i in range(1, 1001):
    tmp = i
    thousand = int(tmp / 1000)
    if thousand > 0:
        ans += dic[1] + dic[1000]
    tmp -= thousand * 1000
    if tmp == 0:
        continue
    hundred = int(tmp / 100)
    tmp -= hundred * 100
    if hundred > 0:
        ans += dic[hundred] + dic[100]
    if tmp == 0:
        continue
    if hundred > 0:
        ans += 3
    if dic.get(tmp, 0) > 0:
        ans += dic[tmp]
        continue
    ten = int(tmp / 10)
    tmp -= ten * 10
    ans += dic[ten * 10] + dic[tmp]

print(ans)
