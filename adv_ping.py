import subprocess
import json
import argparse

def call_and_listen_cpp(cli_app, args, json_key):
    try:
        # Construct the full command with arguments
        command = [cli_app] + args

        # Start the subprocess
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        print(f"Running command: {' '.join(command)}")
        print(f"Listening for JSON data containing key '{json_key}'...")

        # Process stdout line by line
        for line in process.stdout:
            print(f"Raw output: {line.strip()}")  # Debugging: Print raw line
            if json_key in line:
                try:
                    json_data = json.loads(line.strip())
                    print(f"JSON data loaded: {json_data}")
                    return json_data
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON: {line.strip()} Error: {e}")

        # Wait for the process to complete
        process.stdout.close()
        process.wait()

        # Check if there were any errors
        if process.returncode != 0:
            error_output = process.stderr.read()
            print(f"Error from C++ app: {error_output.strip()}")
        else:
            print("C++ process completed without errors.")

    except Exception as e:
        print(f"An error occurred: {e}")

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Call a C++ CLI app and parse JSON output.")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments to pass to the C++ application.")
    parser.add_argument("--json-key", default="json_data_name", help="Key to search for in the JSON output.")

    args = parser.parse_args()
    cpp_app = "/home/yotam/workspace/speedcast-task/cmake-build-debug/PingAdvance"

    json_output = call_and_listen_cpp(cpp_app, args.args, args.json_key)

    if json_output:
        print("Final JSON data in memory:")
        print(json.dumps(json_output, indent=4))
    else:
        print("No valid JSON data found.")
