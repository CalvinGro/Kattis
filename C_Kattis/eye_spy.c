#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <inttypes.h>
// #include "dynamic_arr.h"

// START OF DYNAMIC ARRAY
typedef struct {
    uint16_t x;
    uint16_t y;
} pos;

typedef struct {
    pos *data;
    size_t size;
    size_t capacity;
} Vector;

Vector* create_vector(void) {

    Vector* vector = (Vector*)malloc(sizeof(Vector));
    vector->data = NULL;
    vector->size = 0;
    vector->capacity = 0;
    return vector;
}

void push_vector(Vector *v, pos element) {
    if (v->data == NULL) {
        v->capacity = 1;
        v->data = (pos*)malloc(sizeof(pos));
    }
    else if (v->size >= v->capacity) {
        v->capacity *= 2;
        v->data = (pos*)realloc(v->data, v->capacity*sizeof(pos));
    }

    // Add element
    v->data[v->size] = element;
    v->size++;
}


pos pop_vector(Vector *v) {
    if (v->size <= 0) return (pos){0, 0};
    v->size--;
    return v->data[v->size];
}


pos get_vector(Vector *v, int32_t index) {
    // return 0 if out of bounds
    if (abs(index) >= v->size) return (pos){0, 0};

    // otherwise return value at the index
    if (index != 0) index = index % v->size;
    return v->data[index];
}

bool empty_vector(Vector *v) {return v->size == 0;}

size_t size_vector(Vector *v) {return v->size;}

void free_vector(Vector *v) {
    free(v->data);
    free(v);
}
// END OF DYNAMIC ARRAY


void printGrid(int16_t r, int16_t c, int32_t grid[r][c]) {
    for (int16_t i = 0; i < r; i++) {
        for (int16_t j = 0; j < c; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
}

void printMap(int16_t r, int16_t c, int32_t grid[r][c]) {
    for (int16_t i = 0; i < r; i++) {
        for (int16_t j = 0; j < c; j++) {
            switch (grid[i][j]) {
                case -4: 
                    printf("X");
                    break;
                case -3: 
                    printf("P");
                    break;
                case -2: 
                    printf("#");
                    break;
                case 0: 
                    printf("A");
                    break;
                default: 
                    printf(".");
            }
        }
        printf("\n");
    }
}



int traverseGrid(pos Alex, pos Portal, int16_t r, int16_t c, int32_t grid[r][c]) {

    Vector* cur_pos_vect = create_vector();
    Vector* next_pos_vect = create_vector();
    push_vector(cur_pos_vect, Alex);

    pos rev_search_pos = (pos){Portal.x, Portal.y};

    bool portal_found = false;
    bool alex_found = false;
    uint32_t dist = 0;
    uint32_t next_dist = 0;

    // Preform BFS until portal is found 
    while (!portal_found && !empty_vector(cur_pos_vect)) {
        dist++;

        for (int i=0; i < size_vector(cur_pos_vect); i++) {
            pos cur_pos = get_vector(cur_pos_vect, i);
            int16_t cur_x = cur_pos.x;
            int16_t cur_y = cur_pos.y;

            // First check if the portal is adjacent
            if (
                grid[cur_y-1][cur_x] == -3 ||
                grid[cur_y+1][cur_x] == -3 ||
                grid[cur_y][cur_x-1] == -3 ||
                grid[cur_y][cur_x+1] == -3
            ) {
                portal_found = true;
                next_dist = dist-1;
                break;
            }
            // For each current pos add each surrounding pos avaliable 
            // to the next vector setting their distance from Alex.
            if (grid[cur_y-1][cur_x] == -1) {
                grid[cur_y-1][cur_x] = dist;
                push_vector(next_pos_vect, (pos){cur_x, cur_y-1});
            }
            if (grid[cur_y+1][cur_x] == -1) {
                grid[cur_y+1][cur_x] = dist;
                push_vector(next_pos_vect, (pos){cur_x, cur_y+1});
            }
            if (grid[cur_y][cur_x-1] == -1) {
                grid[cur_y][cur_x-1] = dist;
                push_vector(next_pos_vect, (pos){cur_x-1, cur_y});
            }
            if (grid[cur_y][cur_x+1] == -1) {
                grid[cur_y][cur_x+1] = dist;
                push_vector(next_pos_vect, (pos){cur_x+1, cur_y});
            }
        }

        // Set currect position vector as the next vector.
        // Also set next_pos_vect as a new vector.
        free_vector(cur_pos_vect);
        cur_pos_vect = next_pos_vect;
        next_pos_vect = create_vector();
    }

    free_vector(cur_pos_vect);
    free_vector(next_pos_vect);

    // Now the portal has been found or the cur_pos_vect is empty.
    if (!portal_found) return 0;
    // Search backward from the portal 
    while (!alex_found) {
        // check if adjancent to Alex
        if (
            (rev_search_pos.x-1 == Alex.x && rev_search_pos.y == Alex.y) ||
            (rev_search_pos.x+1 == Alex.x && rev_search_pos.y == Alex.y) ||
            (rev_search_pos.x == Alex.x && rev_search_pos.y-1 == Alex.y) ||
            (rev_search_pos.x == Alex.x && rev_search_pos.y+1 == Alex.y)
        ) {
            alex_found = true;
            break;
        }

        pos lowest_pos;
        // if not adjacent to Alex find surrounding square which is closest to Alex.
        if (grid[rev_search_pos.y-1][rev_search_pos.x] == next_dist) {
            lowest_pos = (pos){rev_search_pos.x, rev_search_pos.y-1};
        } else if (grid[rev_search_pos.y+1][rev_search_pos.x] == next_dist) {
            lowest_pos = (pos){rev_search_pos.x, rev_search_pos.y+1};
        } else if (grid[rev_search_pos.y][rev_search_pos.x-1] == next_dist) {
            lowest_pos = (pos){rev_search_pos.x-1, rev_search_pos.y};
        } else if (grid[rev_search_pos.y][rev_search_pos.x+1] == next_dist) {
            lowest_pos = (pos){rev_search_pos.x+1, rev_search_pos.y};
        } else {
            return 0;
        }
        rev_search_pos = lowest_pos;
        next_dist = grid[lowest_pos.y][lowest_pos.x]-1;
        grid[lowest_pos.y][lowest_pos.x] = -4;
    }

    return 1;
}



int main(void) {

    pos Alex;
    pos Portal;
    uint16_t r, c;
    char line[500];

    fgets(line, 50, stdin);
    sscanf(line, "%" SCNu16 " %" SCNu16, &r, &c);

    int32_t grid [r][c];

    // get grid row input
    for (uint16_t i = 0; i < r; i++) {
        fgets(line, 500, stdin);

        // put each row value into the grid
        for (int32_t j = 0; j < c; j++) {
            switch (line[j]) {
                case '.':
                    grid[i][j] = -1;
                    break;
                case '#':
                    grid[i][j] = -2;
                    break;
                case 'P':
                    grid[i][j] = -3;
                    Portal.x = j;
                    Portal.y = i;
                    break;
                case 'A':
                    grid[i][j] = 0;
                    Alex.x = j;
                    Alex.y = i;
                    break;
                default:
                    break;
            }
        }
    }

    int traverse_status = traverseGrid(Alex, Portal, r, c, grid);
    if (traverse_status == 0) {
        printf("call for help");
    } else {
        printMap(r, c, grid);
    }
}