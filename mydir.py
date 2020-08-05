import os

class MyDir:
    def __init__(self, dir):
        self.dir = dir
        self.files = []
        self.dir_list()

    def dir_list(self):
        with os.scandir(self.dir) as entries:
            for entry in entries:
                self.files.append(entry.name)

    def create_file(self, fname):
        with open("{}/{}".format(self.dir, fname), "w") as f:
            f.write(fname)