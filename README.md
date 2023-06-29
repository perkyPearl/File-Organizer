# File Organizer

This Python script organizes files in a directory based on their file extensions. It reads the `FileExt.txt` file to determine the target folders for each file extension and moves the files accordingly.

## Prerequisites

- Python 3.10

## Libraries Used
- OS: The os module in Python provides a way to interact with the operating system. It offers a range of functions for working with files, directories, and various operating system functionalities. 
- shutil: The shutil module in Python provides a higher-level interface for file operations. It builds on top of the os module and offers additional functions for file copying, moving, archiving, and more. 

## Usage

1. Create a file named `FileExt.txt` in the same directory as the script. Each line in the file should follow the format `Folder Name : Extension`, where `Folder Name` is the desired folder name for files with that extension, and `Extension` is the file extension (e.g., `Documents : pdf`).

2. Run the script using the following command:

   ```
   python Organizer.py
   ```

3. The script will prompt you for commands. Here are the available commands:

   - `start`: Sorts and moves the files according to their file extensions as specified in `FileExt.txt`.
   - `status`: Displays the list of files that are going to be sorted.
   - `logs`: Displays the file movements for the current session.
   - `help`: Shows a list of available commands.
   - `exit`: Exits the program.

   Note: The files `"Organizer.py"` and `"FileExt.txt"` are excluded from sorting.

## Example

Suppose the `FileExt.txt` contains the following lines:

```
Documents : pdf
Pictures : png
Videos : mp4
```

And the directory has the following files:

```
document1.pdf
image1.png
video1.mp4
script.py
```

Running the script and executing the `start` command will organize the files into the respective folders:

```
Documents
    └── document1.pdf
Pictures
    └── image1.png
Videos
    └── video1.mp4
```

The script will also provide information on the number of files moved and folders created.
