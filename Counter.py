#Imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import pandas as pd
import datetime
from pandas import DataFrame

#Point to Directory
csv_dir = '/path/to/csv_dir'

#Point to File
df = pd.read_csv(csv_path + 'file_name', low_memory=False)

# Statistical Analysis
from collections import Counter
Source_port_counts = Counter(df['source_port'])
Destination_port_counts = Counter(df['destination_port'])
print ('Length',Counter(df['source_ip']))

# define the dataset as a string
df1 = str(Source_port_counts)

ports1 = df1.split(", ")
output1 = []

for port in ports1:
    port_num = port.split(":")[0].strip()
    output1.append("source_port:" + port_num)

result1 = ", ".join(output1)

# define the dataset as a string
df2 = str(Destination_port_counts)

ports2 = df2.split(", ")
output2 = []

for port in ports2:
    port_num = port.split(":")[0].strip()
    output2.append("destination_port:" + port_num)

result2 = ", ".join(output2)

# convert the dataset string to a Counter object
dataset_counter1 = Counter(eval(df1))

# get the values as a list and sort them in descending order
values1 = sorted(dataset_counter1.values(), reverse=True)

# convert the dataset string to a Counter object
dataset_counter2 = Counter(eval(df2))

# get the values as a list and sort them in descending order
values2 = sorted(dataset_counter2.values(), reverse=True)

# Define the filename for your output file
filename1 = "/Users/lewis/Desktop/Uni/5th_Year/EM501/PYTHON Code/PortNames/SourcePorts1.txt"

# Open the file for writing and write the output string to it
with open(filename1, "w") as output_file:
    output_file.write(result1)

filename2 = "/Users/lewis/Desktop/Uni/5th_Year/EM501/PYTHON Code/PortNames/Sourcecounts1.txt"

with open(filename2, "w") as output_file:
    output_file.write(str(values1))

filename3 = "/Users/lewis/Desktop/Uni/5th_Year/EM501/PYTHON Code/PortNames/DestinationPorts1.txt"

with open(filename3, "w") as output_file:
    output_file.write(result2)

filename4 = "/Users/lewis/Desktop/Uni/5th_Year/EM501/PYTHON Code/PortNames/Destinationcounts1.txt"

with open(filename4, "w") as output_file:
    output_file.write(str(values2))
