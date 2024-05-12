#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a,b,c;
    ::cin >> a >> b >> c;
    if (pow(a,3) >= b * (pow(c,3))) {
        ::cout << "Yes";
    }
    else {
        ::cout << "No";
    }
    return 0;
}
