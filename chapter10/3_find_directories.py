"""
Algorithm: page 157

Note: When running this script, Python console or terminal must be in
"chapter10" directory, or in the same directory where this script is.
"""

import os


def find_directories_v1(current_directory):

    files = os.listdir()  # get list of filenames in current directory

    for filename in files:
        # if not files:
        if os.path.isfile(os.path.join(current_directory, filename)) == False:
            print(filename)


def find_directories_v2(current_directory):

    files = os.listdir()  # get list of filenames in current directory

    for filename in files:
        # if not files:
        if os.path.isdir(os.path.join(current_directory, filename)) == True:
            for inner_file in os.walk(filename):
                print(f"{inner_file[0]}")


def find_directories_recursive(current_directory):

    subfolders = [f.path for f in os.scandir(current_directory) if f.is_dir()]

    for directory in list(subfolders):
        subfolders.extend(find_directories_recursive(directory))

    return subfolders


if __name__ == "__main__":
    cwd = os.getcwd()
    # cwd = sys.path[0]
    # cwd = os.path.dirname(os.path.realpath(sys.argv[0]))

    print("Version 1:")
    find_directories_v1(cwd)

    print()

    print("Version 2:")
    find_directories_v2(cwd)

    print()

    print("Recursive Version:")
    res = find_directories_recursive(cwd)
    # print(res) # for full path
    # or
    for i in range(len(res)):
        print(f"i = {i}")
        m = res[i]
        while i >= 0:
            temp = []
            h, t = os.path.split(m)
            temp.append(t)
            if os.path.join(h, t) == cwd:
                break
            print(temp, end=" ")
            i -= 1
            m = h
