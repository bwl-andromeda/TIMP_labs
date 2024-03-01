#include <iostream>

int main() {
    int k = 5;
    int m;

    m = ++k + k++ - --k - k--;

    std::cout << "k = " << k << std::endl;
    std::cout << "m = " << m << std::endl;

    return 0;
}