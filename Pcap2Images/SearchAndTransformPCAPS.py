from distutils.filelist import FileList
import os
from UserSetUp import *
from Pcap2ImageFile import *
import pprint

inpath = EXAMPLE_PCAP_FOLDER
outpath = IMAGE_OUTPUT

inputList = []
alreadyDone = []

def listFiles(path):
    filelist = []
    for root, dirs, files in os.walk(path):
	    for file in files:
            #append the file name to the list
		    filelist.append(os.path.join(root,file))
    return filelist

inputList = listFiles(inpath)
alreadyDone = listFiles(outpath)

print('Current length of new files to turn to images is ', len(inputList))
for infile in inputList:
    for donefile in alreadyDone:
       if donefile.replace(colour_suffix, '').replace(gray_suffix,'').replace(IMAGE_OUTPUT,'') in infile:
            inputList.remove(infile)
            break;
print('length of new files to turn to images, minus duplicates is ', len(inputList))


failures =[]
for name in inputList:
    if pcap_extension in name:
        print(name)
        print(name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        f = PCAP2_Image(name, name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        if f != None:
            failures.append(f);
if len(failures) == 0:
    print('All PCAPS converted')
else:
    print('These PCAPS were too large to convert')
    pprint.pprint(failures)