a = 1
for i in range(1, 101):
    a *= i
a_str = str(a)
ans = 0
for i in range(len(a_str)):
    ans += int(a_str[i])
print(ans)