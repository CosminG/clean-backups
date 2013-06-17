clean-backups
=============

Script to delete old backup directories.

The directories names are assumed to be numbers like this: 130601, 130602, 130603, 130604, 130605, 130606.

13 is the year
06 is the month
01 is the day


Create config.py:

 cp config.py.example config.py

Adjust config.py:

backups_dir: the directory where the subdirectories are
Ex.: backups_dir = '/srv/bk/'

how_many_keep: numbers of backup folders to keep
Ex.: how_many_keep = 3

With this configuration the script will delete all the folders in /srv/bk/ leaving only 3 directories witch are more recent.
So it will delete: ['130601', '130602', '130603']
Leaving untouched: 130604  130605  130606