import os  # * we will definitely need this for moving/getting the files
from os.path import join, getsize, splitext
import json # * Needed to get sort criteria from file


parser = argparse.ArgumentParser(description='Sorts all files in a directory')
parser.add_argument('--verbose', '-v', action='count', default=0, help='Enable verbose output')
parser.add_argument('--dir', dest='DirToSort', type=str,  help='The directory you would like to sort')
parser.add_argument('--dest', dest='DestDir', type=str,  help='The directory you would like to sort the files to')
parser.add_argument('--quiet', '-q', action='count', default=0, help='Prevents script from asking for user input. This wil set destination and source to current directory if not otherwise set.')

args = parser.parse_args()

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

def get_file_types(sortdict, ext):  # ex. if ext is ".txt" it return Texts as defined in json file
    for filetype in sortdict:
        for extension in sortdict[filetype]:
            if extension == ext:
                return filetype
    else: return False

def sort_files(files,dir_dest):
    # ! Noah Liby
    # * Sort the list of files
    # I will likely use a dictionary or something.
    # File will be moved to its destination if move_required is set to True
    # Do not forget to set destination path

    # For now, just sort the files that we know need to be sorted, docs, txt, etc
    f = open('sortguide.json', 'r')  # open the json file
    sortdict = json.load(f)  # load the json into a dictionary
    f.close()  # close the json file
    for directory in files:
        for item in files[directory]:
            typ = get_file_types(sortdict, item["ext"])
            if typ:
                item['destination_path'] = f"{dir_dest}/{typ}"
                item['move_required'] = True

    return files


def move_files(files):
    for item in files.items():
        for file in item[1]:
            if file['move_required'] and file['destination_path'] != '':
                if not os.path.isdir(file['destination_path']):  # If dest does not exist, create it
                    os.makedirs(file['destination_path'])
                os.rename(file['original_path'], f"{file['destination_path']}/{file['name']}")


def get_dir():  # gets the directory to sort
    print("Would you like to sort your current directory? [Y/n]")
    choice = input().lower()
    if choice == 'n':
        print("Please enter a directory to sort")
        dir_to_sort = input()
    else:
        dir_to_sort = os.getcwd()
    if not os.path.isdir(dir_to_sort):  # Validate that given directory exists
        print("Directory does not exist")
        return False
    return dir_to_sort

def get_dest_dir():  # Gets a destination directory for the sorted files to go
    print("Would you like the sorted items to be put in your current directory? [Y/n]")
    choice = input().lower()
    if choice == 'n':
        print("Please enter a destination directory")
        dir_dest = input()
    else:
        dir_dest = os.getcwd()
    if not os.path.isdir(dir_dest):  # Validate that given directory exists
        print("Directory does not exist")
        print("Would you like to create the directory? [Y/n]")
        choice = input().lower()
        if choice == 'n':
            return False
        else: # Create the directory
            os.makedirs(dir_dest)  # Create the directory
    return dir_dest


def main():
    # ! Whoever feels like it
    # Just example
    #files = get_files('/Users/alex/Downloads')
    #move_files(sort_files(files))



    # * Noah Liby
    dir_to_sort = False
    while not dir_to_sort:  # While dir_to_sort is not defined, continue calling the get_dir function.
        dir_to_sort = get_dir()
    dir_dest = False
    while not dir_dest:  # While dir_to_sort is not defined, continue calling the get_dir function.
        dir_dest = get_dest_dir()
    files_to_sort = get_files(dir_to_sort)  # Get the files in the given directory
    sorted_files = sort_files(files_to_sort,dir_dest)  # Sort the list of files
    move_files(sorted_files)  # Move the files
    print("Done")


if __name__ == '__main__':  # If script is being run and not imported.
    main()
