#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

LL gcd(LL x, LL y) {
    if (x % y == 0)
        return y;
    else
        return gcd(y, x % y);
}

int main() {
    long long ans = 1;
    for (int i = 1; i <= 20; ++ i)
        ans = ans * i / gcd(ans, i);
    cout << ans << endl;
    return 0;
}
