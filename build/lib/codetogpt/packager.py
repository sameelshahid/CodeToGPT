import os

def concatenate_files(source_folder, output_file, file_extension=".py"):
    """Concatenates all files with the given extension from source_folder into a single file."""
    with open(output_file, 'w') as outfile:
        for subdir, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r') as infile:
                        outfile.write(f"# {file}\n")
                        outfile.write(infile.read() + "\n\n")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Package code into a single file.")
    parser.add_argument("source_folder", type=str, help="The folder containing code files")
    parser.add_argument("output_file", type=str, help="The output file")
    args = parser.parse_args()

    concatenate_files(args.source_folder, args.output_file)

if __name__ == "__main__":
    main()
