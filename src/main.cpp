#include <iostream>

// Inform C++ that the functions in math_operations.c are C functions
extern "C" {
#include "ping.c"  // Include the C source file directly
#include "ping_common.c"
#include "ping_common.h"
}

int main() {
#include <iostream>

    // Declare the C function (renamed to c_main)
    extern "C" {
        int c_main(int argc, char **argv);  // Declare the renamed C main function
    }

    int main(int argc, char **argv) {
        // Call the C function (c_main) from C++
        return c_main(argc, argv);  // Pass argc and argv from C++ main to C function
    }

    return 0;
}

