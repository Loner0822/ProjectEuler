#include <bits/stdc++.h>

using namespace std;

int main() {
    int a = 0;// sum of square
    int b = 0;// square of sum

    for (int i = 1; i <= 100; ++ i) {
        a += i * i;
        b += i;
    }
    b = b * b;
    cout << b - a << endl;
    
    return 0;
}
