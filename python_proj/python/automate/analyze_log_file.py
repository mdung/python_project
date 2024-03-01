import re

# Function to analyze log files for specific patterns or errors
def analyze_log_file(log_file_path, output_file_path, pattern):
    # Open the log file for reading
    with open(log_file_path, 'r') as log_file:
        # Read the entire content of the log file
        log_content = log_file.read()

        # Use regular expressions to find matches for the specified pattern
        matches = re.findall(pattern, log_content)

        # Write the matches to the output file
        with open(output_file_path, 'w') as output_file:
            for match in matches:
                output_file.write(match + '\n')

# Main function
def main():
    # Specify the path to the input log file
    input_log_file_path = 'input/logfile.txt'

    # Specify the path for the output file
    output_file_path = 'output/output.txt'

    # Specify the pattern to search for in the log file (adjust as needed)
    # Example: Searching for lines containing 'ERROR'
    search_pattern = r'\bERROR\b'

    # Analyze the log file
    analyze_log_file(input_log_file_path, output_file_path, search_pattern)

if __name__ == "__main__":
    main()
