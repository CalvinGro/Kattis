
#include <stdint.h>

typedef struct Vector Vector;

typedef struct {
    uint16_t x;
    uint16_t y;
} pos;

Vector* create_vector(void);
void push_vector(Vector*, pos);
pos pop_vector(Vector*);
pos get_vector(Vector*, int32_t);
bool empty_vector(Vector*);
size_t size_vector(Vector*);
void free_vector(Vector*);
