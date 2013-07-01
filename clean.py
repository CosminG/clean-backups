#!/usr/bin/python
import os
import shutil
from library import *


free_space = free_gb(backups_dir)

dirs_list = []

for dir, subdir, filenames in os.walk(backups_dir):
    for dir in subdir:
        if dir.isdigit():
            dirs_list.append(dir)

dirs_list.sort()
# print dirs_list

if min_free_gb > free_space:
    print 'Found ' , free_space , ' free space on ' , backups_dir , ' witch is less than min_free_gb: ' , min_free_gb

    for i in range(how_many_keep):
        if dirs_list:
            dirs_list.pop()

    del_dirs_list = dirs_list

    print 'Directories deleted: '
    print del_dirs_list
    for dir in del_dirs_list:
        shutil.rmtree(backups_dir + dir)

else:
    print 'Found ',free_space,'GB free space on ' , backups_dir , ' witch is more than min_free_gb: ' , min_free_gb , 'GB.'
    print 'No directories will be deleted.'

try:
    (type(del_dirs_list) is list)
except NameError:
    del_dirs = ''
else:
    del_dirs = str(del_dirs_list)[1:-1]

how_many_dirs = len(dirs_list)

data_dic = {
    'date': now_string(),
    'ip': get_lan_ip(),
    'free_space': free_space,
    'c_min_free_gb': min_free_gb,
    'how_many_dirs': how_many_dirs,
    'c_how_many_keep': how_many_keep,
    'del_dirs': del_dirs,
}

print_to_mysql(data_dic)
