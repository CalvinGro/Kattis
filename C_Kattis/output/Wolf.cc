#include <iostream>
#include <string>
#include <sstream>


int main(void) {

    int count;
    std::cin >> count;
    
    int hearts[14] = {0};
    int clubs[14] = {0};
    int spades[14] = {0};
    int diamonds[14] = {0};

    for (int i = 0; i < count; i++) {
        std::string line;
        std::string type;

        std::cin >> line;
        int value = std::stoi(line);

        std::cin >> type;
        
        if (type == "H") hearts[value] = 1;
        else if (type == "C") clubs[value] = 1;
        else if (type == "S") spades[value] = 1;
        else if (type == "D") diamonds[value] = 1;
    }

    if (count > 26) {
        std::cout << "possible";
    } else if (count == 26) {

    // manually check each suit
    bool possible = false;
    bool found_highest = false;
    for (int i = 13; i > 0; i--) {
        if (hearts[i] == 1) {
            found_highest = true;
        } else if (found_highest) {
            possible = true;
        }
    }

    found_highest = false;
    for (int i = 13; i > 0; i--) {
        if (clubs[i] == 1) {
            found_highest = true;
        } else if (found_highest) {
            possible = true;
        }
    }

    found_highest = false;
    for (int i = 13; i > 0; i--) {
        if (spades[i] == 1) {
            found_highest = true;
        } else if (found_highest) {
            possible = true;
        }
    }

    found_highest = false;
    for (int i = 13; i > 0; i--) {
        if (diamonds[i] == 1) {
            found_highest = true;
        } else if (found_highest) {
            possible = true;
        }
    }
    if (possible) {
        std::cout << "possible";
    } else {
        std::cout << "impossible";
    }
    } else {
        std::cout << "impossible";
    }
    return 0;
}