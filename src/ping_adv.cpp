#include <iostream>
#include "ping_common.h"

extern "C" {
    // Declare the c_main function from ping.c
    int c_main(int argc, char** argv);
}

int main(int argc, char** argv) {
    // Example of C++ pre-processing or argument manipulation
    std::cout << "Calling c_main from C++ wrapper...\n";

    // Pass the command-line arguments directly to c_main
    int result = c_main(argc, argv);

    // Handle the return value or errors
    if (result != 0) {
        std::cerr << "c_main returned an error: " << result << "\n";
        return result;
    }

    std::cout << "c_main executed successfully.\n";
    return 0;
}