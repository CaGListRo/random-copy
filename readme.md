# Random File Copy Script

This Python script randomly copies files from a source directory to a destination directory. It ensures that all files in the source directory are copied exactly once in a random order.

## Prerequisites

- Python 3.x
- `shutil` (standard library)
- `os` (standard library)
- `sys` (standard library)
- `random` (standard library)

## Installation

No external libraries are required for this script, as it uses only standard Python libraries.

## Usage

1. Save the script to a file, for example, `random_copy.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `random_copy.py`.
4. Run the script with `python random_copy.py`.
5. Follow the prompts to enter the source and destination paths.

## Example

```sh
$ python random_copy.py
Enter the source path: /path/to/source
Enter the destination path: /path/to/destination
Copied 1 of 10
Copied 2 of 10
...
All files copied.
```

Script Details
The script performs the following steps:

1. Prompts the user to input the source and destination directories.
2. Validates that both the source and destination paths are directories.
3. Collects all files in the source directory.
4. Randomly selects and copies each file from the source to the destination, ensuring each file is copied only once.
5. Prints the progress to the console.
6. Handles any exceptions that occur during the copying process and prints an error message if a file fails to copy.

License
This project is licensed under the MIT License - see the LICENSE file for details.
