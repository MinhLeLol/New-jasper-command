//Hoang Le, October 30, 2025
#include "getbits.h"

/*
 * pprint_binary
 * AKA Pretty Print Binary
 *
 * Input:
 * storage -- a positive integer
 * nlsb -- number of least significant bits to print
 *
 * Note: binary numbers are stored "in reverse"
 * The least significant bit is on the left
 * 1111 0000 0000 0000 
 * ^
 * the ones place
 * Note that the output should have a space after every 4 bits
 * and have the hex value representation in parentheses at the end
 * e.g., 0000 0000 1111 1111 (0xFF)
 */

int pprint_binary(unsigned int storage, unsigned int nlsb)
{
    if (nlsb >= MAX_BITS){
        fprintf(stderr, "The program can only print 32 bits binary.\n");
        printf("Expand your screen to make the boxes fit.\n");
        nlsb = MAX_BITS; 
    }
    if (nlsb == 0){
        printf("(0x00)");
        return 6; //length of "(0x00)", which is the hex of nothing
    }
    FILE *file_handle = fopen("bits_file.txt", "w+");
    if (file_handle == NULL){
        fprintf(stderr, "Failed to open file or file doesn't exist.\n");
        exit(EXIT_FAILURE);
    }
    unsigned mask = 1U; // 1U is unsigned int: 0000 0000 0000 0000 0000 0000 0000 0001
    mask <<= nlsb -1; //Ex; user want 8, but computer onlys know 0 to 7 (equivalent to 8), so we subtract 1.
    int space_count = 0; //Every 4 numbers will add a space
    int char_count_bit = 0; //Count the amout of "character" printed (for the binary part only)
    int hex_count = 0; //Count for the hex part
    int hex_width = 0; //This will count how many block of 0 in the binary so we will use it for hex printing
    for (int i = nlsb - 1; i>= 0; i--){ //Since computer always start at index 0, we need to subtract 1 to start at the last index
        if (space_count == GROUP_OF_0_SIZE){
            printf(" ");
            space_count = 0;
            char_count_bit++;
        }
        fprintf(file_handle,"%c", (storage & mask) ? '1' : '0'); //This line will compare the current bit of the mask to the current bit of the storage, if true (equal in value) print 1 and otherwise
        printf("%c", (storage & mask) ? '1' : '0');
        space_count++;
        char_count_bit++;
        mask >>= 1;
    }
    hex_width = (nlsb+3)/4; //each 4 bits = 1 hex digit, we will need plus 3 for 3 hex digits
    hex_count = printf(" (0x%0*X)", hex_width, storage);
    char_count_bit = char_count_bit + hex_count; //Not count the new-line character
    fclose(file_handle);
    return char_count_bit;
}