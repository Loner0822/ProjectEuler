n = 1000000
vis = [0] * (n + 1)
prime = []
vis[0] = 1
vis[1] = 1
for i in range(2, n + 1):
    if vis[i] == 0:
        prime.append(i)
    for j in range(len(prime)):
        if i * prime[j] > n:
            break
        vis[i * prime[j]] = 1
        if i % prime[j] == 0:
            break
Pow_10 = [1, 10, 100, 1000, 10000, 100000, 1000000]

def Check(num):
    if num < 10:
        return False
    digit = []
    while num > 0:
        digit.append(num % 10)
        num = int(num / 10)
    tmp = 0
    for i in range(len(digit)):
        tmp = tmp + Pow_10[i] * digit[i]
        if vis[tmp] == 1:
            return False
    digit.reverse()
    tmp = 0
    for i in range(len(digit)):
        tmp = tmp * 10 + digit[i]
        if vis[tmp] == 1:
            return False
    return True

ans = 0
for i in prime:
    if Check(i):
        ans += i
        print(i)
print(ans)