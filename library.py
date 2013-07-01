import MySQLdb as mdb
import datetime
import os
import socket
import fcntl
import struct

try:
    from config import *
except ImportError:
    raise ImportError('Create and adjust config.py: cp config.py.example config.py');

def now_string():
    cur_date = datetime.datetime.now() # get datetime type value.
    cur_date = str(cur_date) # transfer datetime value to a str value
    cur_date = cur_date[0:-10]

    return cur_date

def print_to_mysql(data_dic):
    con = mdb.connect(mysql_host, mysql_user, mysql_pass, mysql_db);

    with con:

        cur = con.cursor()
        cur.execute ("""
                INSERT INTO cleanups (
                    date,
                    ip,
                    free_space,
                    c_min_free_gb,
                    how_many_dirs,
                    c_how_many_keep,
                    del_dirs
                )
                VALUES (
                    %(date)s,
                    %(ip)s,
                    %(free_space)s,
                    %(c_min_free_gb)s,
                    %(how_many_dirs)s,
                    %(c_how_many_keep)s,
                    %(del_dirs)s
                )
            """, data_dic)

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                            ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def free_gb(dir):
    s = os.statvfs(dir)
    free_space = (s.f_bavail * s.f_frsize) / 1024 / 1024 / 1024

    return free_space