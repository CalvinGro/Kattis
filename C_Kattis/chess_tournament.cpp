#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <numeric> // for iota

class UnionFind {
private:
    std::vector<uint16_t> parents;
    std::vector<uint16_t> sizes;
    uint16_t condensed_count = 0;

public:
    UnionFind(uint16_t n) 
    : parents(n), sizes(n, 1) {
        std::iota(parents.begin(), parents.end(), 0);  // 0, 1, 2, 3, 4, ...
    }


    uint16_t find(uint16_t n) {
        if (parents[n] != n) {
            parents[n] = find(parents[n]);
        }
        return parents[n];
    }


    void unite(uint16_t a, uint16_t b) {
        uint16_t a_parent = find(a);
        uint16_t b_parent = find(b);

        if (a_parent == b_parent) return;

        if (sizes[a_parent] >= sizes[b_parent]) {
            parents[b_parent] = a_parent;
            sizes[a_parent] += sizes[b_parent];
        } else {
            parents[a_parent] = b_parent;
            sizes[b_parent] += sizes[a_parent];
        }
    }

    
    // WARNING: you can't use find() on a condensed vector 0 -> 0 is not guaranteed
    // instead of having the final reference parents names be 3, 24, 54, 83, ...
    // condense them to 0, 1, 2, 3, 4, ...
    std::vector<uint16_t> condense(void) {
        std::unordered_map<uint16_t, uint16_t> parent_map; // <old parent numbers -> new parent numbers>
        std::vector<uint16_t> new_parents = parents;

        condensed_count = 0;

        for (uint16_t i = 0; i < parents.size(); i++) {
            uint16_t final_parent = find(i);
            
            if (parent_map.find(final_parent) != parent_map.end()) {
                new_parents[i] = parent_map[final_parent];
            } else {
                new_parents[i] = parent_map[final_parent] = condensed_count;
                condensed_count++;
            }
        }

        return new_parents;
    }

    uint16_t get_count(void) {
        return condensed_count;
    }
};

// use index of node as their id
class DirectedGraphWithKahn {
private:
    struct Node {
        std::vector<uint16_t> children;
        uint16_t indegree = 0;
    };
    std::vector<Node> graph;
    
public:
    DirectedGraphWithKahn(uint16_t n): graph(n) {};

    void AddEdge(uint16_t from, uint16_t to) {
        graph[from].children.push_back(to);
        graph[to].indegree++;
    }

    // WARNING: Kahn Search is currently a one time operation 
    //          because it clears all of the .indegree counts.
    bool KahnCycleSearch(void) {
        
        // add all nodes to the queue where deg = 0
        std::queue<uint16_t> q;
        for (uint16_t i = 0; i < graph.size(); i++) {
            if (graph[i].indegree == 0) {
                q.push(i);
            }
        }

        // iterate through q
        while (!q.empty()) {
            uint16_t parent = q.front();
            q.pop();

            for (uint16_t child : graph[parent].children) {
                graph[child].indegree--;
                if (graph[child].indegree == 0) {
                    q.push(child);
                }
            }
        }

        // check if any cycles
        for (Node node : graph) {
            if (node.indegree != 0) return false;
        }
        return true;
    }
};

struct Match{
    uint16_t winner = 0;
    uint16_t loser = 0;
};

int main() {
    std::vector<Match> matches;
    uint16_t p_count = 0;
    uint32_t m_count = 0;
    std::cin >> p_count >> m_count;
    
    UnionFind players(p_count);
    
    // loop through, build matches and union all: a = b
    for (uint32_t i = 0; i < m_count; i++) {
        uint16_t player1 = 0;
        uint16_t player2 = 0;
        char oper = ' ';
        
        std::cin >> player1 >> oper >> player2;

        if (oper != '=') {
            if (oper == '>') {
                matches.emplace_back(player1, player2);
            } else {
                matches.emplace_back(player2, player1);
            }
        } else {
            players.unite(player1, player2);
        }
    }

    // loop through remaining matches and build directed graph
    std::vector<uint16_t> ref_values = players.condense();

    DirectedGraphWithKahn dgk(players.get_count());

    for (Match match : matches) {
        uint16_t winner = ref_values[match.winner];
        uint16_t loser = ref_values[match.loser];

        dgk.AddEdge(winner, loser);        
    }

    bool no_cycle = dgk.KahnCycleSearch();

    if (no_cycle) {
        std::cout << "consistent";
    } else {
        std::cout << "inconsistent";
    }

    return 0;
}