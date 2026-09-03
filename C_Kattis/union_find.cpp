#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <numeric> // for iota


class UnionFind {
private:
    std::vector<uint32_t> parents;
    std::vector<uint32_t> sizes;
    uint32_t condensed_count = 0;

public:
    UnionFind(uint32_t n) 
    : parents(n), sizes(n, 1) {
        std::iota(parents.begin(), parents.end(), 0);  // 0, 1, 2, 3, 4, ...
    }


    uint32_t find(uint32_t n) {
        if (parents[n] != n) {
            parents[n] = find(parents[n]);
        }
        return parents[n];
    }


    void unite(uint32_t a, uint32_t b) {
        uint32_t a_parent = find(a);
        uint32_t b_parent = find(b);

        if (a_parent == b_parent) return;

        if (sizes[a_parent] >= sizes[b_parent]) {
            parents[b_parent] = a_parent;
            sizes[a_parent] += sizes[b_parent];
        } else {
            parents[a_parent] = b_parent;
            sizes[b_parent] += sizes[a_parent];
        }
    }
};

int main() {
    uint32_t n = 0;
    uint32_t q = 0;
    std::cin >> n >> q;


    UnionFind uf(n);

    for (uint32_t i = 0; i < q; i++) {
        char oper = ' ';
        uint32_t v1 = 0;
        uint32_t v2 = 0;
        std::cin >> oper >> v1 >> v2;

        if (oper == '?') {
            if (uf.find(v1) == uf.find(v2)) {
                std::cout << "yes\n";
            } else {
                std::cout << "no\n";
            }
        } else {
            uf.unite(v1, v2);
        }

    }
    return 0;
}