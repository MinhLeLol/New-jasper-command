#include <stdio.h>
#include <stdlib.h>
#include "getbits.h" //This .h file will have all the function definitions and libraries that all .c file can use if include them.

// DO NOT EDIT MAIN
/* Usage: ./mysolution [number] [nlsb]*/

int main(int argc, char *argv[])
{   
    if(argc != 3){
        fprintf(stderr, "Usage: ./mysolution [number] [nlsb]");
        return EXIT_FAILURE;
    }
    unsigned int a = atoi(argv[1]);
    unsigned int nlsb = atoi(argv[2]);

    //pprint_binary(0xFF, 16); // For testing
    int characters = pprint_binary(a, nlsb);
    printf("\nCharacters: %d\n", characters);
    return EXIT_SUCCESS;
}
