#! /usr/bin/python
import os
import shutil

try:
    from config import backups_dir, how_many_keep
except ImportError:
    raise ImportError('Create and adjust config.py: cp config.py.example config.py');

dirs_list = []

for dir, subdir, filenames in os.walk(backups_dir):
    for dir in subdir:
        if dir.isdigit():
            dirs_list.append(dir)

dirs_list.sort()
# print dirs_list

for i in range(how_many_keep):
    if dirs_list:
        dirs_list.pop()

print "Directories deleted: "
print dirs_list
for dir in dirs_list:
    shutil.rmtree(backups_dir + dir)