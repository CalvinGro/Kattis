
#include <iostream>
#include <cstdint>
#include <string>
#include <vector>

struct Line {
    int a;
    int_fast32_t b;
    int c;
};

struct Point {
    int x;
    int y;
};

bool is_above_line(Line line, Point pnt) {
    int xline = line.a * pnt.x + line.b * pnt.y - line.c;
    return (xline > 0);
}

Line create_line(int x1, int y1, int x2, int y2) {
    // line standard form
    int a = (y1-y2);
    int b = (x2-x1);
    int c = (x2*y1) - (x1*y2);
    Line ln = {a,b,c};
    return ln;
}

int main() {

    // collect lines
    int s = 0;
    std::cin >> s;

    std::vector<Line> lines;
    
    for (int i = 0; i < s; i++) {
        int x1, y1, x2, y2;

        std::cin >> x1 >> y1 >> x2 >> y2;
        Line ln = create_line(x1, y1, x2, y2);
        lines.push_back(ln);
    }


    // collect and compare points
    int t = 0;
    std::cin >> t;
    
    for (int i = 0; i < t; i++) {
        int x1, y1, x2, y2;

        std::cin >> x1 >> y1 >> x2 >> y2;
        
        Point p1 = {x1, y1};
        Point p2 = {x2, y2};

        // start on same side true
        // every oposite side flips same_designation
        // try every line
        bool same_designation = true;
        for (int j = 0; j < s; j++) {
            Line curln = lines[j];
            if (is_above_line(curln, p1) != is_above_line(curln, p2)) {
                if (same_designation) {
                    same_designation = false;
                } else {
                    same_designation = true;
                }
            }
        }

        if (same_designation) {
            std::cout << "same\n";
        } else {
            std::cout << "different\n";
        }
    }    
    return 0;
}