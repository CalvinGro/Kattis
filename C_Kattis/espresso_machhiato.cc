#include <iostream>
#include <string>
int main(void) {
    int t = 0;

    std:: cin >> t;

    for (int i = 0; i < t; i++) {
        int n = 0;

        std::cin >> n;

        std::string line1;
        std::string line2;
        for (int k = 0; k < n; k++) {
            line1 += ".";
            line2 += ".";
        }

        line1[1] = 'c';
        line2[0] = 'c';

        std::cout << line1 << "\n";
        std::cout << line2 << "\n";

        std::string line;
        for (int k = 0; k < n; k++) {
            line += ".";
        }


        for (int j = 2; j < n; j++) {
            std::cout << line << "\n";
        }
    }

    return 0;
}