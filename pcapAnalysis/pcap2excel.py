#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:25:46 2022

@author: lewis
"""

import os
import shutil
import sys
from pcap_splitter.splitter import PcapSplitter as ps



sys.displayhook = lambda x: None

#Location of directory to copy from
location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap'
os.chdir(location)

#File type 
file_type = 'pcap'
file_type = '.'+file_type
file_type2 = 'json'
file_type2 = '.'+file_type2

#Location to copy to 
copy_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move'

#Location to split to
split_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move/split'
location2 = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move/2'

#Location of Renamed Files
rename_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move/rename'


#Check the file exists
for fname in os.listdir('.'):
    if fname.endswith('.pcap'):
        break
else:
    pass

#Check if file is finished writing
if os.access(copy_location, os.W_OK):
    pass
else:
    pass

#Move the file and split it based on Source ip
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        shutil.copy(filename, copy_location)
        pcapsplit = ps(filename)
        print(pcapsplit.split_by_ip_src_dst("move/split"))

    else:
        pass

#Remove files to prevent copies
os.chdir(split_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove empty files
os.chdir(split_location)
for filename in os.listdir('.'):
    if os.path.getsize(filename) == 0:
        os.remove(filename)
else:
    pass

#Rename Files
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        base = os.path.basename(filename)
        start = os.path.splitext(base)[0]
        shutil.move(filename, location2)
        os.chdir(location2)
        source = os.popen('ls | awk \'{system("tshark -r "$1" -T fields -e ip.src | tail -1")}\'').read()
        newname = start + '_' + source + '.pcap'        
        newname = os.rename(filename, newname)
        for file in os.listdir('.'):
            if file.endswith(file_type):
                shutil.move(file, rename_location)
        os.chdir(split_location)
