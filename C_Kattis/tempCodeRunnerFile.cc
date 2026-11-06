#include <algorithm>
#include <vector>
#include <iostream>


std::vector<int> nums = {2,34,3,4,334,532};

int main() {
    std::ranges::sort(nums);

    for (int num : nums) {
        std::cout << num << " ";
    };

    return 0;
}