ans = 0
n = 2000000
vis = [0] * (n + 1)
prime = []
for i in range(2, n + 1):
    if vis[i] == 0:
        prime.append(i)
        ans += i
    for j in range(len(prime)):
        if i * prime[j] > n:
            break
        vis[i * prime[j]] = 1
        if i % prime[j] == 0:
            break
print(ans)