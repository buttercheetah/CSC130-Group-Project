import os  # * we will definitely need this for moving/getting the files
from os.path import join, getsize, splitext


def get_file_info(file, directory):
    return {
        "name": file,
        "size": getsize(join(directory, file)),
        "ext": splitext(file)[1],
        "original_path": join(directory, file),
        "destination_path": "",
        "move_required": False,
    }


def get_files(directory):
    # * Get a complete list of files in a given directory. For now, ignore directorys
    files_dict = {}

    for root, dirs, files in os.walk(directory):
        files_dict[root] = [get_file_info(item, root) for item in files]

    return files_dict


def sort_files(files):
    # ! Noah Liby
    # * Sort the list of files
    # I will likely use a dictionary or something.
    # File will be moved to its destination if move_required is set to True
    # Do not forget to set destination path
    return files


def move_files(files):
    for item in files.items():
        for file in item[1]:
            if file['move_required'] and file['destination'] != '':
                os.rename(file['source'], file['destination'])


def GetDir():
    print("Would you like to sort your current directory? [Y/n]")
    choice = input().lower()
    if choice == 'n':
        print("Please enter a directory to sort")
        DirToSort = input()
    else:
        DirToSort = os.getcwd()
    if not os.path.isdir(DirToSort):  # Validate that given directory exists
        print("Directory does not exist")
        return False
    return DirToSort


def main():
    # ! Whoever feels like it
    # Just example
    files = get_files('/Users/alex/Downloads')
    move_files(sort_files(files))

    # * Noah Liby
    # DirToSort = False
    # while not DirToSort:  # While DirToSort is not defined, continue calling the GetDir function
    #     DirToSort = GetDir()
    # FilesToSort = get_files(DirToSort)  # Get the files in the given directory
    # SortedFiles = SortFiles(FilesToSort)  # Sort the list of files
    # MoveFiles(SortedFiles)  # Move the files
    # print("Done")


if __name__ == '__main__':  # If script is being run and not imported.
    main()
