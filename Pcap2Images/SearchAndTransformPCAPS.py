from distutils.filelist import FileList
import os
from UserSetUp import *
from Pcap2ImageFile import *
import pprint

inpath = './PLC_Packets/'
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
       if os.path.basename(infile).replace('.pcap', '') in donefile:
           if infile in inputList:
               inputList.remove(infile)
print('length of new files to turn to images, minus duplicates is ', len(inputList))

#For each input convert the pcap to an image, keep of list of files that were to big to convert
failures =[]
for name in inputList:
    if pcap_extension in name:
        print(name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        f = createBufferImages(name, name.split(filePath_slash)[len(name.split(filePath_slash))-1].replace(pcap_extension,''))
        if f != None:
            failures.append(f);
if len(failures) == 0:
    print('All PCAPS converted')
else:
    print('These PCAPS were too large to convert')
    pprint.pprint(failures)
    
    
    
    