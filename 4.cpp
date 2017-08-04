#include <bits/stdc++.h>

using namespace std;

template<typename T> string toString(const T& t) {
    ostringstream oss;
    oss << t;
    return oss.str();   
}

bool Check(int tmp) {
    string s = toString(tmp);
    for (int i = 0; i < (int)s.size(); ++ i)
        if (s[i] != s[(int)s.size() - i - 1])
            return 0;
    return 1;
}

int main() {
    int ans = 0;
    for (int i = 100; i <= 999; ++ i)
        for (int j = 100; j <= 999; ++ j) {
            int tmp = i * j;
            if (Check(tmp))
                ans = max(ans, tmp);
        }
    cout << ans << endl;
    return 0;
}
