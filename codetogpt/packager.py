import os
import argparse

def concatenate_files(source_folder):
    """Concatenates Python and Java files from source_folder into separate output files."""
    python_output_file = os.path.join(source_folder, "combined_python_code.txt")
    java_output_file = os.path.join(source_folder, "combined_java_code.txt")

    # Collect all contents first to check if they are non-empty
    python_contents = collect_files_contents(source_folder, ".py")
    java_contents = collect_files_contents(source_folder, ".java")

    # Write contents to files if non-empty
    if python_contents:
        write_contents_to_file(python_contents, python_output_file)
        print(f"Combined Python file created at: {python_output_file}")
    else:
        print("No Python files found or all were empty.")

    if java_contents:
        write_contents_to_file(java_contents, java_output_file)
        print(f"Combined Java file created at: {java_output_file}")
    else:
        print("No Java files found or all were empty.")

def collect_files_contents(source_folder, file_extension):
    """Collects and returns the contents of all files with the given extension in the source folder."""
    contents = []
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r') as infile:
                    file_contents = infile.read()
                    if file_contents.strip():  # Check if the file is not just whitespace
                        contents.append((file_path, file_contents))
    return contents

def write_contents_to_file(contents, output_file):
    """Writes the collected contents to the specified output file with a header for each file."""
    with open(output_file, 'w') as outfile:
        for file_path, file_contents in contents:
            relative_path = os.path.relpath(file_path, os.path.dirname(output_file))
            outfile.write(f"# File: {relative_path}\n")
            outfile.write(file_contents + "\n\n")

def main():
    parser = argparse.ArgumentParser(description="Separately package Python and Java code into single files.")
    parser.add_argument("source_folder", type=str, help="The folder containing code files")
    args = parser.parse_args()

    concatenate_files(args.source_folder)

if __name__ == "__main__":
    main()
