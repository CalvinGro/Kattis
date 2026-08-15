#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <inttypes.h>
#include <stdbool.h>
#include "dynamic_arr.h"


struct Vector {
    pos *data;
    size_t size;
    size_t capacity;
};

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

