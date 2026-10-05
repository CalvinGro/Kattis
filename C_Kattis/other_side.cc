#include <iostream>
#include <string>

int main(void) {
    int w=0, s=0, c=0, k=0;
    std::cin >> w >> s >> c >> k;
    if (s < k || w + c < k || (s <= k && c + w <= 2 * k) || (w + c == k && s <= 2 * k)) std::cout << "YES";
    else std::cout << "NO";
    return 0;
}