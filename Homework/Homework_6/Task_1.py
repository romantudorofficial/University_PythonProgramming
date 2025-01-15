import os
import sys

def find_and_read_files(directory, extension):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")
        
        # Check if the extension is valid
        if not extension.startswith('.'):
            raise ValueError("File extension must start with a '.'")

        # Search for files with the given extension
        files_found = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
        if not files_found:
            print(f"No files with the extension '{extension}' found in '{directory}'.")
            return

        # Read and print contents of each file
        for file_path in files_found:
            try:
                with open(file_path, 'r') as file:
                    print(f"\nContents of {file_path}:\n{'-'*40}")
                    print(file.read())
            except Exception as e:
                print(f"Could not read file '{file_path}': {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        find_and_read_files(directory_path, file_extension)
