import os # * we will definitely need this for moving/getting the files

def GetFilesInDir(dir):
    #! Alexander Rodin 
    # * Get a complete list of files in a given directory. For now, ignore directorys
    pass

def SortFiles(files):
    #! Noah Liby
    # * Sort the list of files
    # I will likely use a dictionary or something.
    pass

def MoveFiles(files):
    #! Noah Liby
    # * Move the list of files to purposefull location
    pass

def GetDir():
    print("Would you like to sort your current directory? [Y/n]")
    choice = input().lower()
    if choice == 'n':
        print("Please enter a directory to sort")
        DirToSort = input()
    else:
        DirToSort = os.getcwd()
    if not os.path.isdir(DirToSort): # Validate that given directory exists
        print("Directory does not exist")
        return False
    return DirToSort

def main():
    #! Whoever feels like it

    #* Noah Liby
    DirToSort = False
    while not DirToSort: # While DirToSort is not defined, continue calling the GetDir function
        DirToSort = GetDir()
    FilesToSort = GetFilesInDir(DirToSort) # Get the files in the given directory
    SortedFiles = SortFiles(FilesToSort) # Sort the list of files
    MoveFiles(SortedFiles) # Move the files
    print("Done")

if __name__ == '__main__': # If script is being run and not imported.
    main()