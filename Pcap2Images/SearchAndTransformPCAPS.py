import os
from UserSetUp import *
from Pcap2ImageFile import *

path = EXAMPLE_PCAP_FOLDER
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    print(name)
    print(name.split('\\')[1].replace('.pcap',''))
    PCAP2_Image(name, name.split('\\')[1].replace('.pcap',''))