#include <iostream>
#include <iomanip>
#include "ping_common.h"

extern "C" {
    // Declare the c_main function from ping.c
    advanced_statistics c_main(int argc, char** argv);
}

int main(int argc, char** argv) {
    // Example of C++ pre-processing or argument manipulation
    std::cout << "Calling c_main from C++ wrapper...\n";

    // Pass the command-line arguments directly to c_main
    auto result = c_main(argc, argv);

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "result number: " << result.result_number <<" average latency: " << result.avarage_latency << "ms, average jitter: " << result.avarage_jitter <<" ms"<< std::endl;


    std::cout << "c_main executed successfully.\n";
    return 0;
}