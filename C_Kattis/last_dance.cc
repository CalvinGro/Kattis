#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>

int main() {
    int t;
    std::cin >> t;
    for (int c = 0; c < t; c++) {
        int n, sq, g;
        std::cin >> n >> sq >> g;

        std::unordered_map<int, int> people;
        for (int i = 0; i < sq; i++) {
            char sq_type;
            int genre;
            std::cin >> sq_type >> genre;
            int count = 0;

            if (sq_type == 'Q') {
                for (const auto& [person, last_gen] : people) {
                    if (last_gen == genre) count ++;
                }
                std::cout<< count << "\n";
            } else {
                int a, b;
                std::cin >> a;

                std::string line;
                std::getline(std::cin, line);
                std::istringstream stream(line);
                while (stream >> b) {
                    people[b] = genre;
                }
                for (int j = 0; j < a; j++) {
                    std::cin >> b;
                    people[b] = genre;
                }
            }
        }
    }
}