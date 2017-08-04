#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int M = 800000 + 10;

LL tot = 0, Prime[M];
bool vis[M];


void get_Prime() {
    memset(vis, 0, sizeof vis);
    for(int i = 2; i <= 800000; ++ i) {
        if (vis[i] == 0) {
            Prime[++tot] = i;
            for (int j = 1; j * i <= 800000; ++ j)
                vis[j * i] = 1;
        }
    }
}

int main() {
    LL ans = 0ll;
    get_Prime();
    LL num = 600851475143;
    for (int i = 1; i <= tot; ++ i)
        if (num % Prime[i] == 0)
            ans = max(ans, Prime[i]);
    cout << ans << endl;
    return 0;
}
