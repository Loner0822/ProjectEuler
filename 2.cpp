#include <bits/stdc++.h>

using namespace std;

int main() {
    int F1, F2, F3, sum = 0;
    F1 = F2 = 1;
    while(F1 < 4000000) {
        F3 = F2, F2 = F1;
        F1 = F2 + F3;
        if ((F1 & 2) == 0)
            sum += F1;
    }
    cout << sum << endl;
    return 0;
}
