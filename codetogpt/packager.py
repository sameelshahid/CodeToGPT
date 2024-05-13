import os
import argparse

def concatenate_files(source_folder):
    """Concatenates Python and Java files from source_folder into separate output files."""
    python_output_file = os.path.join(source_folder, "combined_python_code.txt")
    java_output_file = os.path.join(source_folder, "combined_java_code.txt")

    # Initialize files to ensure they are empty before starting
    open(python_output_file, 'w').close()
    open(java_output_file, 'w').close()

    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                write_contents_to_file(file_path, python_output_file, source_folder)
            elif file.endswith(".java"):
                file_path = os.path.join(subdir, file)
                write_contents_to_file(file_path, java_output_file, source_folder)

    print(f"Combined Python file created at: {python_output_file}")
    print(f"Combined Java file created at: {java_output_file}")

def write_contents_to_file(file_path, output_file, source_folder):
    """Writes the contents of a file to the specified output file with a header."""
    relative_path = os.path.relpath(file_path, source_folder)  # Compute the relative path
    with open(output_file, 'a') as outfile:  # Open in append mode
        # Write relative path and file name as a comment for reference
        outfile.write(f"# File: {relative_path}\n")
        with open(file_path, 'r') as infile:
            outfile.write(infile.read() + "\n\n")  # Read and write the contents of the file

def main():
    parser = argparse.ArgumentParser(description="Separately package Python and Java code into single files.")
    parser.add_argument("source_folder", type=str, help="The folder containing code files")
    args = parser.parse_args()

    concatenate_files(args.source_folder)

if __name__ == "__main__":
    main()
