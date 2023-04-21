from Pcap2ImageFile import *
from UserSetUp import *
from distutils.filelist import FileList
import os
from UserSetUp import *
from Pcap2ImageFile import *
import pprint
import random

path ='C:\\Users\\callu\\Documents\\Python Scripts\\Building\\Pcap2Images\\Example_PCAPS\\SQLIATTACKS\\1_CM_sqli_easy_p_.pcap'
fileName = path.split(filePath_slash)[len(path.split(filePath_slash))-1].replace(pcap_extension,'')


inpath = './PLC_Packets/PLC_SCAN/'
outpath = IMAGE_OUTPUT

inputList = []
alreadyDone = []

#Return a list of files in a set of folders and those folders sub-folders
def listFiles(path):
    filelist = []
    for root, dirs, files in os.walk(path):
	    for file in files:
            #append the file name to the list
		    filelist.append(os.path.join(root,file))
    return filelist

#Create a list of pcap files to transform
inputList = listFiles(inpath)
#Create a list of images that have already been transformed in the output
alreadyDone = listFiles(outpath)

#Remove already transformed images from input list
print('Current length of new files to turn to images is ', len(inputList))
for infile in inputList:
    for donefile in alreadyDone:
       if donefile.replace(colour_suffix, '').replace(gray_suffix,'').replace(IMAGE_OUTPUT,'') in infile:
            inputList.remove(infile)
            break;
print('length of new files to turn to images, minus duplicates is ', len(inputList))

#For each input convert the pcap to an image, keep of list of files that were to big to convert
failures =[]
buff = [] 
name = None

random.shuffle(inputList)

for name in inputList:
    if pcap_extension in name:
        print(name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        f = createBufferImages(name, name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''), buff, name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        if type(f) is str:
            failures.append(f);
        else:
            name = f[0].replace(pcap_extension,'')
            buff = f[1]
            #print(name)
if len(failures) == 0:
    print('All PCAPS converted')
else:
    print('These PCAPS were too large to convert')
    pprint.pprint(failures)
    
    
    
    