a = pow(2, 1000)
a_str = str(a)
ans = 0
for i in range(len(a_str)):
    ans += int(a_str[i])
print(ans)