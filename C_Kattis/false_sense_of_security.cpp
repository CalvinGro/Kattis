#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <bitset>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>


void toggle_encryption(std::vector<uint8_t>& char_lens) {

    std::reverse(char_lens.begin(), char_lens.end());
}


uint16_t set_bits_in_bitset(std::bitset<4000>& buffer, std::string line, std::vector<uint8_t>& char_lens, std::unordered_map<char, std::string>& bits_map) {
    uint16_t bitset_index = 0;

    // for each char add the correct bits to the bit set.
    for (uint16_t i = 0; i < line.size(); i++) {
        std::string morse_code = bits_map[line[i]];
        char_lens.push_back(morse_code.size());

        for (uint8_t j = 0; j < morse_code.size(); j++) {
            
            if (morse_code[j] == '1') buffer.set(bitset_index);
            else buffer.reset(bitset_index);
            bitset_index++;
        }
    }
    return bitset_index;
}


void print_words_in_bitset(std::bitset<4000>& buffer, std::vector<uint8_t>& char_lens, std::unordered_map<std::string, char>& letters_map) {
    std::string final_msg = "";
    uint16_t bitset_index = 0;
    std::string cur_bits;

    // add each char to the final_msg string from the bitset.
    for (uint16_t i = 0; i < char_lens.size(); i++) {
        // for each char.
        cur_bits = "";

        for (uint8_t j = 0; j < char_lens[i]; j++) {
            // for each bit of the current char.
            cur_bits += buffer[bitset_index] ? '1' : '0';
            bitset_index++;
        }

        // now using the char's bits get the char.
        // then add it to the final msg
        final_msg += letters_map[cur_bits];
    }

    std::cout << final_msg << "\n";
}


int main() {

    std::unordered_map<std::string, char> letters_map = {
        {"01", 'A'}, {"1000", 'B'}, {"1010", 'C'}, {"100", 'D'},
        {"0", 'E'}, {"0010", 'F'}, {"110", 'G'}, {"0000", 'H'},
        {"00", 'I'}, {"0111", 'J'}, {"101", 'K'}, {"0100", 'L'},
        {"11", 'M'}, {"10", 'N'}, {"111", 'O'}, {"0110", 'P'},
        {"1101", 'Q'}, {"010", 'R'}, {"000", 'S'}, {"1", 'T'},
        {"001", 'U'}, {"0001", 'V'}, {"011", 'W'}, {"1001", 'X'},
        {"1011", 'Y'}, {"1100", 'Z'}, {"0011", '_'}, {"1110", '.'},
        {"0101", ','}, {"1111", '?'}
    };

    std::unordered_map<char, std::string> bits_map;
    bits_map.insert({'A', "01"});
    bits_map.insert({'B', "1000"});
    bits_map.insert({'C', "1010"});
    bits_map.insert({'D', "100"});
    bits_map.insert({'E', "0"});
    bits_map.insert({'F', "0010"});
    bits_map.insert({'G', "110"});
    bits_map.insert({'H', "0000"});
    bits_map.insert({'I', "00"});
    bits_map.insert({'J', "0111"});
    bits_map.insert({'K', "101"});
    bits_map.insert({'L', "0100"});
    bits_map.insert({'M', "11"});
    bits_map.insert({'N', "10"});
    bits_map.insert({'O', "111"});
    bits_map.insert({'P', "0110"});
    bits_map.insert({'Q', "1101"});
    bits_map.insert({'R', "010"});
    bits_map.insert({'S', "000"});
    bits_map.insert({'T', "1"});
    bits_map.insert({'U', "001"});
    bits_map.insert({'V', "0001"});
    bits_map.insert({'W', "011"});
    bits_map.insert({'X', "1001"});
    bits_map.insert({'Y', "1011"});
    bits_map.insert({'Z', "1100"});
    bits_map.insert({'_', "0011"});
    bits_map.insert({'.', "1110"});
    bits_map.insert({',', "0101"});
    bits_map.insert({'?', "1111"});

    std::string line;
    while (std::getline(std::cin, line)) {
        std::vector<uint8_t> char_lens;
        std::bitset<4000> buffer;

        uint16_t bitset_index = set_bits_in_bitset(buffer, line, char_lens, bits_map);
        toggle_encryption(char_lens);
        print_words_in_bitset(buffer, char_lens, letters_map);
    }
}