#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <inttypes.h>


int main(void) {


    char line[20];
    uint32_t storage;
    uint32_t apples;
    uint32_t kms = 1;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%" SCNu32 " %" SCNu32, &apples, &storage);

    while(apples > 0) {
        apples -= (apples + storage - 1) / storage;
        kms += 1;
    }
    printf("%d", kms);
}