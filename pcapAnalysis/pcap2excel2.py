#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:30:18 2022

@author: lewis
"""

import os
import shutil
import sys
import json
import pandas as pd
from pandas import json_normalize
import glob


sys.displayhook = lambda x: None

#Location of directory to copy from
location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap'

#File type 
file_type = 'pcap'
file_type = '.'+file_type
file_type2 = 'json'
file_type2 = '.'+file_type2
file_type3 = 'csv'
file_type4 = '_pcap'

#Location to copy to 
copy_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move'

#Location of Renamed Packets
rename_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move/rename'

#Location of Malicious Packets
malicious_location = '/Users/maxfawcett/Desktop/Lupovis/ML/pcap/move/rename/Malicious'

#Location to put Json Files
json_location = '/Users/maxfawcett/Desktop/Lupovis/ML/json'

#Convert to Json files
os.chdir(malicious_location)
os.system('ls | awk \'{system("tshark -r "$1" -T json > " $1 ".json")}\'')
print("File's converted to Json")

#Move to Json Folder
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        shutil.move(filename, json_location)
        print("Json Files moved")
else:
    pass

#Remove empty files
os.chdir(json_location)
for filename in os.listdir('.'):
    if os.path.getsize(filename) == 0:
        os.remove(filename)
else:
    pass

#Json Parsing
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        with open(filename, 'r') as json_data:
            data = json.load(json_data)

        try:
            for frame in data:
                del frame['_source']['layers']['frame']
        except KeyError:
            pass

        try:
            for null in data:
                del null['_source']['layers']['null']
        except KeyError:
            pass

        try:
            for score in data:
                del score['_score']
        except KeyError:
            pass

        try:
            for type in data:
                del type['_type']
        except KeyError:
            pass

        with open(filename, 'w') as f:
            json.dump(data, f)

else:
    pass

#Remove files to prevent copies
os.chdir(location)
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove files to prevent copies
os.chdir(copy_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove files to prevent copies
os.chdir(malicious_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove files to prevent copies
os.chdir(rename_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove files to prevent copies
os.chdir(malicious_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        os.remove(filename)
        print("File's Removed")
else:
    pass

os.chdir(json_location)
result = list()
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        with open(filename, 'r') as json_data:
            result.extend(json.load(json_data))

with open('_pcap.json', 'w') as output_file:
    json.dump(result, output_file)

#Json to CSV
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        with open(filename) as f:
            data = json.load(f)
            df = json_normalize(data)
            df.to_csv('_pcap.csv', index=False)
else:
    pass

#Merge to one CSV File
all_filenames = [i for i in glob.glob('*.{}'.format(file_type3))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "all_pcap.csv", index=False, encoding='utf-8-sig')


#Remove files to prevent copies
os.chdir(json_location)
for filename in os.listdir('.'):
    if filename.endswith(file_type2):
        os.remove(filename)
        print("File's Removed")
else:
    pass

#Remove files to prevent copies
for filename in os.listdir('.'):
    if filename.startswith(file_type4):
        os.remove(filename)
else:
    pass
