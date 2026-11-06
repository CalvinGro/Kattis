#include <iostream>
#include <cstdint>
#include <unordered_set>
#include <vector>
#include <numeric>
#include <unordered_map>
class Graph {

    enum class BranchType {
        lineage,
        non_lineage
    };

public:
    enum class GraphType {
        bowtie,
        square
    };

    std::vector<uint16_t> cycles; // axes = 0
    uint16_t cycle_i = 1;
    std::vector<uint16_t> dead_end_heads;
    std::vector<uint8_t> checked;
    std::vector<std::unordered_set<uint16_t>> edges; 
    GraphType graph_type = GraphType::square;
    
    // bit of a work around
    std::vector<uint16_t> possible_axes;

    explicit Graph(uint16_t gsize) {
        edges.resize(gsize);
        dead_end_heads.resize(gsize);
        cycles.resize(gsize, 2);
        checked.resize(gsize, 0);
        std::iota(dead_end_heads.begin(), dead_end_heads.end(), 0);
    }
    
    // must build graph and run find_cycs() first
    uint8_t count_paths_between(uint16_t a, uint16_t b) {
        // if on the same lineage
        uint8_t num_of_paths = 0;
        
        a = dead_end_heads[a];
        b = dead_end_heads[b];

        if (a == b) num_of_paths = 1;
        

        // if on separate sides of the axes
        else if (cycles[a] != 1 && cycles[b] != 1 && cycles[a] != 0 && cycles[b] != 0 && cycles[a] != cycles[b]) {
            num_of_paths = 4;
        }

        // for bowtie graphs
        else if (graph_type == GraphType::bowtie) {
            //std::cout << "bowtie\n\n";
            if (cycles[a] == cycles[b] && (cycles[a] == 0 || cycles[b] == 1)) {
                num_of_paths = 1; 
                //std::cout << "set to 1\n";
            } else if (dead_end_heads[a] == dead_end_heads[b] && (dead_end_heads[a] == 0 || dead_end_heads[a] == 0)) {
                num_of_paths = 1;
            } else num_of_paths = 2; 
        }
        // for square graphs
        else num_of_paths = 3;

        return num_of_paths;
    }

    void add_edge(uint16_t a, uint16_t b) {        
        edges[a].insert(b);
        edges[b].insert(a); 
    }



    // clean up all remaining dead ends
    // reset checked to 0 to say that it is checked
    void bfs_all_DEs(void) {

        uint16_t cyc_head = 0;
        for (uint16_t node = 1; node < checked.size(); node++) {
            // skip if already checked
            if (checked[node] == 0) continue;
            if (cycles[node] == 2) continue;

            std::unordered_set<uint16_t>& cur_children = edges[node];

            // set group equal to cycle head
            for (uint16_t child : cur_children) {
                if (cycles[child] != 2) continue;
                _rec_dfs_DEs(node, child, node);
            }            
        }
    }

    // another messy method, this one to varify the type of the graph when there are 2 axes.
    // checks if there are multiple ways, or just one to the other axis
    void determine_type(void) {
        uint8_t axes_count = 0;

        for (uint16_t node = 1; node < checked.size(); node++) {
            if (cycles[node] == 1) continue;
            
            // for node in cycle determine if axis
            std::unordered_set<uint16_t>& cur_children = edges[node];

            
            uint8_t lineage_count = 0;
            for (const uint16_t child : cur_children) {
                if (dead_end_heads[child] == dead_end_heads[node]) continue;
                lineage_count++;
            }

            if (lineage_count >= 3) {
                //std::cout << "found axis at: " << node << "\n\n";
                cycles[node] = axes_count;

                // set it and all de children to 0 cycle num.
                for (const uint16_t de_child : cur_children) {
                    if (dead_end_heads[de_child] != node) continue;
                    _rec_dfs_axes(de_child, axes_count);
                }
                axes_count++;
            }
        }

        if (axes_count == 1) graph_type = GraphType::bowtie;
        else graph_type = GraphType::square;
    
    }


    // finds cycles and adds them to their respective lists
    void find_cycs(void) {
        std::vector<uint16_t> stack;
        std::unordered_set<uint16_t> stack_mems;
        stack.reserve(edges.size());
        stack_mems.reserve(edges.size());

        _rec_dfs_find(0, 1, stack, stack_mems);
    }

private:
    // given a node that is not in a cycle recurse through it's tree
    void _rec_dfs_DEs(
        uint16_t prev,
        uint16_t parent, 
        uint16_t cyc_node
    ) {
        std::unordered_set<uint16_t>& cur_children = edges[parent];

        // set to lineage value
        dead_end_heads[parent] = cyc_node;
        
        if (cycles[parent] != 2) return;


        for (const uint16_t child : cur_children) {
            if (child == prev) continue;
            
            else {
                _rec_dfs_DEs(parent, child, cyc_node);
            }
        }
    }


    void _rec_dfs_axes(
        uint16_t parent, 
        uint16_t axis
    ) {
        std::unordered_set<uint16_t>& cur_children = edges[parent];


        uint16_t prev_val = cycles[parent];

        // set to lineage value
        cycles[parent] = axis;        


        for (const uint16_t child : cur_children) {
            if (dead_end_heads[child] != 2) continue;
            
            else {
                _rec_dfs_axes(child, axis);
            }
        }
    }


    void _rec_dfs_find(
        uint16_t prev,
        uint16_t parent, 
        std::vector<uint16_t>& cur_stack, 
        std::unordered_set<uint16_t>& cur_stack_mems
    ) {
        //std::cout << "recursing to node: " << parent << "\n\n";

        std::unordered_set<uint16_t>& cur_children = edges[parent];
        checked[parent] = 1;

        // first add to stack
        cur_stack.push_back(parent);
        cur_stack_mems.insert(parent);

        for (const uint16_t child : cur_children) {
            // skip parent
            if (child == prev) continue;

            // check if cycle
            if (cur_stack_mems.contains(child)) {
                //std::cout << "found cycle at node: " << parent << " with child: " << child << "\n\n";
                _rec_cycle(cur_stack.size()-1, child, cur_stack);
                //std::cout << "added cycle at node: " << parent << "\n\n";
                continue;
            }
            // skip if already checked, but not new cycle
            if (checked[child] != 0) continue;
            _rec_dfs_find(parent, child, cur_stack, cur_stack_mems);
        }
        //std::cout << "finished children for node: " << parent << "\n";
        // rm parent from stack
        cur_stack.pop_back();
        cur_stack_mems.erase(parent);
    }

    void _rec_cycle(uint16_t cur_i, uint16_t end_node, std::vector<uint16_t>& cur_stack) {
        //std::cout << "current stack i: " << cur_i << "\n";

        cycles.at(cur_stack.at(cur_i)) += cycle_i;

        //std::cout << "cur_stack succeeded\n\n";

        if (cur_stack.at(cur_i) != end_node) {
            _rec_cycle(cur_i-1, end_node, cur_stack);
        } else {
            // if reached end node
            cycle_i++;
        }
    }

    void _rec_lineage(uint16_t prev, uint16_t last_child, std::vector<uint16_t>& children_in_a_line) {
        std::unordered_set<uint16_t>& cur_children = edges[last_child];

        // if hit end of lineage
        if (cur_children.size() >= 3) {
            // loop through children in the lineage and add document in dead end vector
            for (uint16_t child : children_in_a_line) {
                dead_end_heads[child] = last_child;
            }

        // else add and continue
        } else {
            children_in_a_line.push_back(last_child);

            for (const uint16_t child : cur_children) {
                if (child != prev) {
                    _rec_lineage(last_child, child, children_in_a_line);
                }
            }

        }
    }
};



int main() {
    uint16_t n = 0, q = 0;

    std::cin >> n >> q;

    Graph graph(n+1);

    // for each edge add it
    for (uint16_t i = 0; i < n+1; i++) {
        uint16_t a, b;
        std::cin >> a >> b;
        graph.add_edge(a,b);
    }

    //std::cout << "started build\n\n";

    graph.find_cycs();
    graph.bfs_all_DEs();
    graph.determine_type();

    std::cout << "finished build\n\n";
    if (graph.graph_type == Graph::GraphType::square) std::cout << "Square\n\n";
    else std::cout << "Bowtie\n\n";
    std::cout << "Dead Ends\n";
    for (uint16_t i = 0; i < graph.dead_end_heads.size(); i++) {
        std::cout << i << ": " << graph.dead_end_heads[i] << "\n";
    }
        std::cout << "\nCycles\n";
    for (uint16_t i = 0; i < graph.cycles.size(); i++) {
        std::cout << i << ": " << graph.cycles[i] << "\n";
    }

    // for each query
    for (uint16_t j = 0; j < q; j++) {
        uint16_t a, b;
        std::cin >> a >> b;

        uint8_t count = graph.count_paths_between(a, b);
        
        std::cout << static_cast<unsigned int>(count) << "\n";
    }

    return 0;
}