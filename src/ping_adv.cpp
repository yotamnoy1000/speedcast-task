#include <iostream>
#include <iomanip>
#include <fstream>
#include "ping_common.h"
#include "json.hpp"

extern "C" {
    // Declare the c_main function from ping.c
    advanced_statistics c_main(int argc, char** argv);
}

std::string getCurrentTimestamp() {
    auto now = std::chrono::system_clock::now();
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);

    std::ostringstream oss;
    oss << std::put_time(std::gmtime(&now_time), "%Y-%m-%dT%H:%M:%SZ");
    return oss.str();
}

int main(int argc, char** argv) {
    // Example of C++ pre-processing or argument manipulation
    std::cout << "Calling c_main from C++ wrapper...\n";

    // Namespace alias for convenience
    namespace fs = std::filesystem;

    // Pass the command-line arguments directly to c_main
    auto result = c_main(argc, argv);

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "result number: " << result.result_number <<" average latency: " << result.avarage_latency << " ms, average jitter: " << result.avarage_jitter <<" ms"<< std::endl;

    nlohmann::ordered_json jsonData = {
        {"json_data_name", "adv_ping_data"},
        {"timestamp", getCurrentTimestamp()},
        {"packet_count", argv[2]},
        {"interval_between_packets", argv[4]},
        {"latency_average", result.avarage_latency},
        {"jitter_average", result.avarage_jitter},
        {"number_of_results", result.result_number}
    };

    std::cout << jsonData << std::endl;
}