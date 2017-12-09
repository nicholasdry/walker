############################
#
# walker.py
# Nicholas Dry
#
############################
import os
import ftplib

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
        files = os.listdir("/".join(self.current_path))
        for file in files:
            if os.path.isdir(os.path.join("/".join(self.current_path), file)):
                if file == "__pycache__": # bunk, go away.
                    continue
                if file[0] == '.':
                    continue
                if file in self.closed_folders:
                    continue
                folder = file
                self.closed_folders.append(folder)
                self.current_path.append(folder)
                self.index()
                self.current_path = self.current_path[:-1]
            else:
                extension = str(file.split(".")[-1:][0])
                if extension not in self.file_index:
                    # Set the key first.
                    self.file_index[extension] = []
                    self.file_index[extension].append(file)
                else:
                    # Add it to the already existing list.
                    self.file_index[extension].append(file)

    def collapse_dictionary(self):
        output = []
        for key in self.file_index.keys():
            for file in self.file_index[key]:
                output.append(file)
        return output