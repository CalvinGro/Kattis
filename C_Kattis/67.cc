#include <iostream>
#include <string>
#include <cstdint>
#include <algorithm>

int main(void) {

    int n = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int output = 0;
        std::string num;
        std::cin >> num;
        
        int first = 0;
        std::reverse(num.begin(), num.end());

        for (int a = 0; a < num.length(); a++) {
            if ((static_cast<int>(num[a]) - static_cast<int>('0')) >= first - 1) {
                first = static_cast<int>(num[a]) - static_cast<int>('0');
            } else {
                first = (static_cast<int>(num[a]) - static_cast<int>('0')) + 1;
            }
        }


        if ((10-first) < num.length()) {
            for (int j = 1; j < (num.length() + 2); j++) {
                output += j;
                output *= 10;
            }

        } else {
            for (int j = 0; j < num.length(); j++) {
                output += first;
                first++;
                output *= 10;
            }
        }
        std::cout << output / 10 << "\n";
    }
    return 0;
}