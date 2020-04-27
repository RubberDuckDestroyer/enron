import os
from email.parser import Parser

rootdir = "C:\\Users\\maxfr\\Desktop\\2020-Enron-Journal\\maildir\\lay-k"

for directory, subdirectory, filenames in os.walk(rootdir):
    print(directory, subdirectory, len(filenames))