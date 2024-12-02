import subprocess
import json
import itertools

def call_and_listen_cpp(cli_app, args, json_key):
    """
    Calls a C++ CLI app with the specified arguments, listens to its stdout for JSON, and returns parsed JSON data.

    Args:
        cli_app (str): Path to the C++ CLI application.
        args (list): Arguments to pass to the CLI application.
        json_key (str): Key to search for in the application's stdout.

    Returns:
        dict: Parsed JSON object if found, otherwise None.
    """
    try:
        # Construct the full command with arguments
        command = [cli_app] + args

        # Start the subprocess
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        print(f"Running command: {' '.join(command)}")

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
    # Path to the C++ CLI application
    cpp_app = "./build/PingAdvance"

    # Define the range of arguments
    packet_counts = range(2, 3)  # -c values from 2 to 50
    intervals = [round(i * 0.1, 1) for i in range(1, 10)]  # -i values from 0.1 to 10.0

    # Define a fixed target (you can adjust this as needed)
    target = "www.google.com"

    # List to store captured JSON data
    captured_data = []

    # Iterate over all combinations of arguments
    for packet_count, interval in itertools.product(packet_counts, intervals):
        args = [target, "-c", str(packet_count), "-i", str(interval)]
        print(f"Testing with args: {args}")

        # Call the C++ app with these arguments
        json_output = call_and_listen_cpp(cpp_app, args, "json_data_name")

        # If valid JSON is found, save it to the list
        if json_output:
            captured_data.append(json_output)

    # Perform further analysis on captured data
    print(f"\nCaptured {len(captured_data)} JSON results.")
    print("Sample data for review:")
    print(json.dumps(captured_data[:5], indent=4))  # Print the first 5 entries as a sample

    # Optionally, save the data to a file for later use
    with open("captured_data.json", "w") as outfile:
        json.dump(captured_data, outfile, indent=4)
    print("All captured data saved to 'captured_data.json'.")
