#! /usr/bin/python
import os
import shutil

try:
    from config import backups_dir, how_many_keep, min_free_gb
except ImportError:
    raise ImportError('Create and adjust config.py: cp config.py.example config.py');

s = os.statvfs(backups_dir)
free_space = (s.f_bavail * s.f_frsize) / 1024 / 1024 / 1024

if min_free_gb > free_space:
    print 'Found ' , free_space , ' free space on ' , backups_dir , ' witch is less than min_free_gb: ' , min_free_gb

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

    print 'Directories deleted: '
    print dirs_list
    for dir in dirs_list:
        shutil.rmtree(backups_dir + dir)

else:
    print 'Found ',free_space,'GB free space on ' , backups_dir , ' witch is more than min_free_gb: ' , min_free_gb , 'GB.'
    print 'No directories will be deleted.'
