#include <bits/stdc++.h>

using namespace std;

const int N = 1000000 + 10;

int Prime[N], tot = 0;
bool vis[N];

int main() {

    for (int i = 2; i <= 1000000; ++ i) {
        if (vis[i] == 0) {
            Prime[tot ++] = i;
            for (int j = 1; j * i <= 1000000; ++ j)
                vis[i * j] = 1;
        }
        if (tot == 10001) {
            cout << Prime[10000] << endl;
            return 0;
        }
    }

    return 0;
}
