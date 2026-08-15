#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

uint16_t count_1s(uint32_t num) {
    uint16_t count = 0;
    uint32_t par_mask = 0x00000001;
    for (uint16_t i = 0; i < 32; i++) {
        if ((par_mask & num) == par_mask) count++;
        num >>= 1;
    }
    return count;
}

uint16_t count_max_1s(uint32_t num) {
    uint16_t max_count = 0;
    uint16_t count = 0;
    do {
        count = count_1s(num);
        if (count > max_count) max_count = count;

        num = num / 10;
    } while (num != 0);
    return max_count;
}

int main() {
    char line[20];
    uint16_t num_count = 0;
    uint32_t num = 0;

    fgets(line, sizeof(line), stdin);
    sscanf(line, "%" SCNu16, &num_count);

    while (num_count > 0) {
        num_count--;

        fgets(line, sizeof(line), stdin);
        sscanf(line, "%" SCNu32, &num);
        uint16_t num_1s = count_max_1s(num);
        printf("%" PRIu16 "\n", num_1s);
    }
}