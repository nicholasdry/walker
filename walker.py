############################
#
# walker.py
# Nicholas Dry
#
############################
import os

class Walker:
    def __init__(self, start_path="."):
        self.start_path = start_path
        self.closed_folders = []
        self.current_path = [self.start_path]
        self.file_index = {}

    def parent_directory(self):
        return os.listdir(self.start_path)

    # This method returns you a dictionary of every file type in the directory
    def index(self):
        # Start by listing all files in the current directory
        # print("Now we are in {0}".format("/".join(self.current_path)))
        # cont = input("> ")
        files = os.listdir("/".join(self.current_path))
        for file in files:
            # print(os.path.isdir(os.path.join("/".join(self.current_path), file)))
            if os.path.isdir(os.path.join("/".join(self.current_path), file)):
                # print("{0} is a folder".format(file))
                if file == "__pycache__": # bunk, go away.
                    continue
                if file[0] == '.':
                    # ignore dotfiles
                    continue
                if file in self.closed_folders:
                    # We have already explored this one, don't go back in
                    continue
                # print("We hit our first folder, let's go in.")
                folder = file
                self.closed_folders.append(folder)
                self.current_path.append(folder)
                self.index()
                self.current_path = self.current_path[:-1]
            else:
                # print("{0} is not a folder".format(file))
                extension = str(file.split(".")[-1:][0])
                # print("Looking at {0}".format(file))
                # cont = input("> ")
                if extension not in self.file_index:
                    # Set the key first.
                    self.file_index[extension] = []
                    self.file_index[extension].append(file)
                else:
                    # Add it to the already existing list.
                    self.file_index[extension].append(file)

    def print_info(self):
        for key in self.file_index.keys():
            print("{0} has {1} files".format(key, len(self.file_index[key])))